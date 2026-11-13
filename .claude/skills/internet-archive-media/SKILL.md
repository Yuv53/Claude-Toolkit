---
name: internet-archive-media
description: Find public-domain footage, audio and images on the Internet Archive (Prelinger, NASA, newsreels) for b-roll and archival material.
---

# Internet Archive media search

- Search: `python3 .claude/skills/internet-archive-media/scripts/archive_org.py search "query" --type movies|audio|image|texts --n 10`
- Files: `python3 .claude/skills/internet-archive-media/scripts/archive_org.py files IDENTIFIER` prints download URLs.
- Defaults to public-domain-licensed items, Prelinger and NASA collections. `--any` removes the filter; much of archive.org is NOT public domain, so verify rights on the item page before using anything found that way.
- Record title, identifier and license for each clip used.
