# AI Session Transcript — make.fun bounty "Sum up 24 November's world news in one image" (v2)

## Session overview

- **Bounty:** Sum up 24 November's world news in one image (https://make.fun/bounty/news-image-20261124)
- **AI assistant:** Muse (Meta)
- **Date:** 2026-11-24 (Beijing time)
- **Repository:** to be created by the user when submitting (same pattern as 20261123: github.com/lhy66976697-cell/news-image-20261124); this v2 replaces the earlier 7-story poster version of the same day.
- **Files produced:** `main.py`, `news-20261124.jpg`, `README.md`, `transcript.md`, `makefun-run.json`, plus the build files `stories.json`, `template.html`, `render.py`, `render.html`, `draft-text.md`, `preview-300.png`

## Direction and decisions (by the user, Li Haoyu)

The user directed the work and made the key creative decisions. Muse (the AI agent) executed the build: researching the winning entries, gathering the news, writing the copy draft, building the template, and verifying determinism.

The user's standing decisions, applied in this run:

- Enter this bounty daily and set the goal: summarize the day's world news in one image.
- Use the Chinese classical visual style (rice paper, ink wash, muted tones) — chosen after the neon first draft was rejected as too garish on 23 November.
- Image text in English, since the bounty is judged in English.
- Focus on AI developments and stock moves, citing Nvidia as the lead story.
- On 24 November the user asked Muse to study the bounty winners so the work can be improved step by step, and then chose to rebuild the 24 November entry with the winners' template instead of submitting the earlier 7-story poster version.
- Text polish is done by Gemini via the web app (gemini.google.com), not the API; the draft text is provided in `draft-text.md` for that step.

## Build log

### 1. Winners research

Muse reviewed the leaderboards of the 19–22 November bounties and read 9 entries in full (4 winners, 2 top-10, 1 mid-rank, 2 low-rank). Full analysis: `~/workspace/makefun-news-image/winners-analysis.md`. The winners all use the same square newspaper front-page template: the date as the largest text, a masthead stating story and region counts, 29–37 dated stories with sources and credibility labels, a UTC timeline, a numbers bar, a dotted world map, and a DATE CHECK footer listing the big stories excluded because they happened on an earlier day. No winning image contains opinion or commentary.

### 2. News selection

Expanded the 24 November list from 7 to 29 stories. Every story happened or was first reported on Tuesday 24 November 2026 (UTC), each with a named source (Reuters / AP / AFP / BBC / WSJ / NYT / SCMP / USGS / UN News / Naharnet / Politico / Kyiv Independent) and a credibility label (CONFIRMED / OFFICIAL / REPORTED / CLAIM). Single-sided accounts are labelled CLAIM, never stated as fact. No commentary of any kind.

The DATE CHECK footer lists the big stories deliberately left out because they happened earlier: Nvidia's 31.5% surge and Huang's reinstatement (Mon 23 Nov), FIFA naming the 2031 and 2035 Women's World Cup hosts (Mon 23 Nov), the UN chief's AI framework call (Mon 23 Nov), COP31 ending without a pact (Sun 22 Nov), Australia's Women's Rugby League World Cup final win (Sun 22 Nov), fighting trapping Ebola responders in Ituri (WHO post Sun 23 Nov), and the US blacklisting Singapore cloud firm Megaspeed (Mon 23 Nov). The old v1 entry's Guterres AI-framework story and Women's World Cup story were both 23 November events, so they were moved from the main list to this exclusion list.

### 3. Text draft

All display copy was drafted in English and saved in `draft-text.md` for polishing via the Gemini web app. No Gemini API call was made (the free tier is rate-limited).

### 4. Template and rendering

Built a reusable HTML/CSS front-page template (`template.html`) driven by `stories.json`. `render.py` fills the template and screenshots it at 1024x1024 with headless Chromium (Playwright). The dotted world map and the small field icons are drawn in code (SVG); the Chinese classical style survives only as a light skin (rice-paper background, ink colours, a red seal).

### 5. Verification

- `main.py` passes `py_compile`.
- Two renders output identical bytes matching the image (SHA-256: c1a493819228b1d9da289af636b62a1f532abf50f02535b7938cbf997fdef92e); a second full re-run produced the same SHA-256 again.
- Image within size limits (1024x1024 JPEG, 341,611 bytes; <=1024x1024 and <=1 MiB).
- Content fits the frame exactly (measured body height 1024px, no clipping); a 300px-wide preview (`preview-300.png`) was checked for small-size readability — date, headline, numbers and story titles stay legible.
- No account was registered, nothing was submitted, and no wallet was touched during this preparation. The GitHub repository and the make.fun submission are handled by the user himself, from mobile Chrome with his Phantom wallet. Deadline: 2026-11-26 08:00 Beijing time.

### 6. Gemini polish and re-render

- The draft in `draft-text.md` was polished by Gemini 4 Neon via the web app; the polished copy is saved in `polished-text.md` and applied to `stories.json` (21 wording edits: spec "ALL FROM ONE DAY", lead "NVIDIA PARES GAINS AS RALLY COOLS", Trump "claims", #3/#4/#5/#6/#10 wording, #15–17/#19–21 full verbs, #23/#25/#27 wording, timeline "warns of", DATE CHECK "UN chief calls for", legend CLAIM "unverified one-sided account"). All 29 stories, facts, numbers, dates, sources and labels unchanged.
- First polished render overflowed by 9px (body height 1033px) and clipped the footer footnote "Scenes are drawn illustrations, not photographs." Fixed by tightening section padding in `template.html` (rule/timeline/numbers/main-grid/also/bottom/legend spacing, no content change) and re-rendered.
- Final verification: 1024x1024 JPEG, 349,529 bytes; two renders byte-identical (SHA-256 808f5cf6c7bbfcbc5ccd86108b053fff5479c275e1466f160953ed5c0006b992); body height exactly 1024px, no clipping; 300px preview checked — date, headline, numbers and story titles stay legible.

## Known limitations of this v1 template

- The dotted world map is a coarse hand-built land mask; continent shapes are approximate and the three pins clustered on the US east coast (New York, Washington, Virginia) sit close together.
- Main-story illustrations are small line icons drawn in code, not pictures; swapping in generated illustrations per story is a possible later upgrade.
- The date is 38px and the lead headline 26px — both smaller than the winners' equivalents — because 29 stories, a timeline, a numbers bar, a map and a DATE CHECK all have to share one 1024x1024 frame.
