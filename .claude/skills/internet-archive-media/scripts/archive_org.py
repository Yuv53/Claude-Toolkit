#!/usr/bin/env python3
"""Search the Internet Archive (stdlib only, no API key). Defaults to public-domain
licensed items. Usage:
  archive_org.py search "query" [--type movies|audio|image|texts] [--n 10] [--any]
  archive_org.py files IDENTIFIER
Download URL for a file: https://archive.org/download/IDENTIFIER/FILENAME"""
import argparse, json, sys, urllib.parse, urllib.request

PD = '(licenseurl:(*publicdomain*) OR collection:(prelinger) OR collection:(nasa))'

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "creative-toolkit/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("query")
    s.add_argument("--type", default="movies"); s.add_argument("--n", type=int, default=10)
    s.add_argument("--any", action="store_true", help="do not restrict to public-domain/NASA/Prelinger")
    f = sub.add_parser("files"); f.add_argument("identifier")
    a = p.parse_args()
    if a.cmd == "search":
        q = f'({a.query}) AND mediatype:{a.type}' + ("" if a.any else f' AND {PD}')
        params = [("q", q), ("rows", a.n), ("output", "json"), ("sort[]", "downloads desc")]
        params += [("fl[]", x) for x in ("identifier", "title", "licenseurl", "creator", "year")]
        d = get("https://archive.org/advancedsearch.php?" + urllib.parse.urlencode(params))
        for it in d["response"]["docs"]:
            print(f'{it["identifier"]} | {it.get("title")} | {it.get("year")} | license: {it.get("licenseurl", "check item page")}')
            print(f'   https://archive.org/details/{it["identifier"]}')
    else:
        d = get(f"https://archive.org/metadata/{urllib.parse.quote(a.identifier)}")
        print("license:", d.get("metadata", {}).get("licenseurl", "none stated - verify rights"))
        for fl in d.get("files", []):
            if fl.get("format") in ("MPEG4", "h.264", "MP3", "VBR MP3", "JPEG", "Ogg Vorbis", "512Kb MPEG4"):
                print(f'{fl["name"]} ({fl.get("format")}, {fl.get("size")} bytes)')
                print(f'   https://archive.org/download/{a.identifier}/{urllib.parse.quote(fl["name"])}')

if __name__ == "__main__":
    sys.exit(main())
