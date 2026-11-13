# creative-toolkit (private)

Skills for Claude covering web design, SEO and marketing, motion graphics, sound and stock media. Attach this repo to a Claude session and everything in `.claude/skills/` is available. See `CLAUDE.md` for which skill to use, and `THIRD_PARTY.md` for sources, commits and licenses.

## Optional keys (nothing requires them)
- SEO: free Google APIs (PageSpeed, Search Console, GA4) give real field data.
- Stock media: Pexels and Freesound API keys are free; Openverse and Internet Archive need none.
- Sound: `earshot` / `real-sound` need `pip install earshot` (local CPU, large model downloads).
- Provide keys in chat for the session; never commit them.

## Not included on purpose
- `morluto/rea` (reverse engineering): needs local binaries and runs processes with your permissions. Add it on a computer you control.
- VoiceStudio: a local desktop app (AGPL, model weights have their own licenses).
- Paid or key-gated pieces: DataForSEO/Ahrefs/SE Ranking SEO extensions, Lots of Sounds.
- Remotion is free for individuals and small teams only; read `remotion-license` before client work.
