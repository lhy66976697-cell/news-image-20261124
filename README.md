# World News — 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/lhy66976697-cell/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/lhy66976697-cell/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entered on [make.fun](https://make.fun/bounty/news-image-20261124) — "Sum up 24 November's world news in one image".

A one-page newspaper front page summarising 24 November 2026 in 29 dated stories.
The image `news-20261124.jpg` is the entry; `main.py` outputs it
deterministically. The news text on the image is in English. Layout follows the
front-page template used by the recent winning entries: masthead with the story
count, the date as the largest text, a lead story, a UTC timeline, a numbers
bar, 13 main stories with sources and credibility labels, a numbered list to
29 stories, a dotted world map, a DATE CHECK footer listing the big stories
left out because they happened on an earlier day, and a legend for the
CONFIRMED / OFFICIAL / REPORTED / CLAIM labels. The visual skin is Chinese
classical (rice paper, ink, a red seal) over that structure. No commentary,
facts only.

## The 29 stories

Lead: **Nvidia pares gains as rally cools** — shares fall about 5% in
early New York trading after Monday's 31.5% surge; Trump claims he "made the
deal" to bring Huang back (CLAIM); Congress presses ahead with its China chip
probe.

Main stories (#2–13): Israeli strikes kill Hamas security chief Abu Nahel;
Russian strike kills 2, wounds 40, including children; NATO vows to defend
against space threats; hacked data points to nearly 500,000 Russian war dead;
Virginia and Oregon sue SpaceX over Grok images; Seoul offers $375,000 to
catch AI exam cheats; US report finds an AI-powered China campaign on the
Taiwan vote; M5.4 quake shakes Nepal, felt in five countries; Russian jets
enter South Korea's air zone; two arrested after a break-in at Prince
William's home; Germany first to access Ukraine's Delta war system; Huckabee
doubts the pledge to end $3.8bn Israel aid.

Also on 24 November (#14–29): Russia says it downed nearly 700 Ukrainian
drones; Latvia on a possible tipping point; Poland on Russian sabotage;
Amnesty on Tigray; UN probe call on Benghazi; Iraq oilfields order; US plan
to train Syrian soldiers in demining; Senate probe into the Vance/Vitol
Venezuela oil deal; Arm extends CEO Rene Haas's tenure; Hanoi blast kills 6;
landmine casualties hit a five-year high of 7,000; Germans reject a choice
between the US and China; Hasina plans to return on 16 December; Japan to pay
full 2027 ICC contribution early; GTA VI hacker walks free; Australia to
treat AI as a key foreign policy issue.

## How to run

```sh
python3 main.py > news.jpg
```

The program only reads the bundled image and writes its bytes to stdout.
No network access, no randomness — running it twice produces identical bytes.

## How the image was made

The page is drawn in code, not generated as a picture: `stories.json` holds
the 29 stories, `template.html` is the reusable front-page template, and
`render.py` fills it and screenshots it at 1024x1024 with headless Chromium.
Two renders produce byte-identical JPEGs (SHA-256 in `makefun-run.json`).
`draft-text.md` is the English copy draft; `polished-text.md` is the
Gemini-polished copy now on the image.

## Sources

- Reuters, 24 November 2026 (Nvidia slip; Gaza strikes; Zaporizhzhia; Grok
  lawsuits; Huckabee; hacked war toll; Latvia; Iraq; Syria demining; Vance
  probe; Hasina)
- BBC, 24 November 2026 (NATO space defence)
- South China Morning Post, 24 November 2026 (hacked data; UK break-in; GTA
  VI hacker; landmine casualties; Germans on US/China; Australia AI policy)
- The Wall Street Journal, 24 November 2026 (South Korea AI exam rewards)
- The New York Times, 24 November 2026 (AI-powered campaign on Taiwan vote)
- AP, 24 November 2026 (Russian jets in South Korea air zone)
- USGS / National Centre for Seismology, 24 November 2026 (Nepal quake)
- Kyiv Independent, 24 November 2026 (Germany / Delta system)
- UN News, 24 November 2026 (Benghazi probe)
- Naharnet, 24 November 2026 (Hanoi blast)
- Politico, 24 November 2026 (Poland on Russian sabotage)
