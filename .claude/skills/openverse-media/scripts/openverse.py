#!/usr/bin/env python3
"""Search Openverse (openly licensed images & audio). Stdlib only, no API key.
Usage: openverse.py {images|audio} "query" [--n 8] [--any-license] [--download DIR]
Default filters to licenses allowing commercial use + modification."""
import argparse, json, os, sys, urllib.parse, urllib.request

def main():
    p = argparse.ArgumentParser()
    p.add_argument("kind", choices=["images", "audio"])
    p.add_argument("query")
    p.add_argument("--n", type=int, default=8)
    p.add_argument("--any-license", action="store_true", help="include non-commercial/no-derivs")
    p.add_argument("--download", metavar="DIR")
    a = p.parse_args()
    params = {"q": a.query, "page_size": min(a.n, 20)}
    if not a.any_license:
        params["license_type"] = "commercial,modification"
    url = f"https://api.openverse.org/v1/{a.kind}/?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "creative-toolkit/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    for i, it in enumerate(data.get("results", [])):
        lic = ('CC ' + str(it.get('license')).upper() + ' ' + str(it.get('license_version') or '')).strip()
        print(f'[{i}] {it.get("title")} | {lic} | by {it.get("creator")} | {it.get("foreign_landing_url")}')
        print(f'     file: {it.get("url")}')
        print(f'     attribution: {it.get("attribution")}')
        if a.download:
            os.makedirs(a.download, exist_ok=True)
            ext = os.path.splitext(urllib.parse.urlparse(it["url"]).path)[1] or (".mp3" if a.kind == "audio" else ".jpg")
            fn = os.path.join(a.download, f'{it["id"]}{ext}')
            urllib.request.urlretrieve(it["url"], fn)
            with open(os.path.join(a.download, "ATTRIBUTION.txt"), "a") as f:
                f.write(f'{os.path.basename(fn)}: {it.get("attribution")}\n')
            print(f"     saved: {fn}")
    if not data.get("results"):
        print("no results")

if __name__ == "__main__":
    sys.exit(main())
