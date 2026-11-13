---
name: openverse-media
description: Find openly licensed (Creative Commons / public domain) images, sound effects, and music from Openverse with ready-to-paste attribution. Use for stock photos, SFX, ambience, or music for websites, videos, and motion graphics.
---

# Openverse media search

Run `python3 .claude/skills/openverse-media/scripts/openverse.py {images|audio} "query" [--n 8] [--download DIR] [--any-license]`.

- No API key. Defaults to licenses that allow commercial use and modification.
- Every result prints license, creator, source page, direct file URL and attribution text.
- `--download DIR` saves files and appends credits to `DIR/ATTRIBUTION.txt`.
- CC BY / BY-SA require credit: always keep the attribution line and tell the user. Never use `--any-license` results commercially without checking.
- If a request is blocked by the network allowlist, say so and ask the user to attach the file instead.
