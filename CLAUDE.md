# Creative toolkit

Private toolkit for web design, SEO/marketing, motion graphics, sound and stock media. Skills live in `.claude/skills/` and load automatically in any session attached to this repo.

Rules for Claude:
- Telemetry is disabled in `.claude/settings.json`. Do not re-enable it.
- Never run `curl | bash` installers. Never put API keys in files; ask the user to provide them in chat for the session only.
- Credit CC-BY / BY-SA assets (use the attribution text the media scripts print).
- Do not copy another site's code, images, copy or branding. Extract structure and tokens only, then rebuild with original assets.
- Remotion needs a paid license for companies above the free tier. Check `remotion-license` before commercial client work.
- Put each project in its own folder under `projects/`; keep rendered media out of git (see `.gitignore`).

Which skill for what:
- Websites: `ui-ux-pro-max`, `web-design-guidelines`, `vercel-react-best-practices`, `vercel-composition-patterns`, `vercel-react-view-transitions`, `gsap-*`
- SEO: `seo` (entry point), `seo-*`; content: `blog`, `blog-*`
- Motion/video: `hyperframes` (main), `hyperframes-cli`, `hyperframes-registry`, `media-use`, `style-sampling`, `slideshow`, `remotion-*`
- Sound: `openverse-media`, `internet-archive-media`, `earshot`, `real-sound` (the last two need `pip install` of earshot)
