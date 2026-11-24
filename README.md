# World News — 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/lhy66976697-cell/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/lhy66976697-cell/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entered on [make.fun](https://make.fun/bounty/news-image-20261124) — "Sum up 24 November's world news in one image".

A Chinese classical-style daily brief summarising the top world news of 24 November 2026.
The image `news-20261124.jpg` is the entry; `main.py` outputs it
deterministically. The news text on the image is in English. Layout is hierarchical:
the lead story (Nvidia / Trump) gets a large central headline with a sharp commentary,
the other stories appear in smaller type, and the smallest item sits in a corner.

## The 7 stories

1. **Trump claims the Nvidia deal** — Trump says he brokered Jensen Huang's return as Nvidia CEO; Vance tapped as his emissary to Nvidia's board. NVDA jumped 31.5% on 23 Nov (best day since May 2003, about $952bn in market value added); Nasdaq +6.5%, S&P 500 +4.7%, Dow +1,448 points.
2. **States sue Musk's Grok** — Virginia and Oregon sue SpaceX over Grok generating sexualised images, including more than 20,000 said to depict children; first states to sue.
3. **UN chief: AI rules in a year** — António Guterres urges a global AI risk-management framework within 12 months.
4. **NATO vows space defence** — Allies warn Russia may launch a nuclear-armed satellite next month.
5. **War toll nears 500,000** — Hacked data puts Russian deaths in Ukraine near half a million; Moscow warns Estonia its actions are on the verge of triggering open war; Kyiv-region strikes kill at least 14.
6. **Women's World Cup 2031** — USA, Mexico, Costa Rica and Jamaica to host the 2031 edition; the UK hosts 2035.
7. **GTA VI hacker walks free** — Arion Kurtaj, 21, gets a 7-year sentence but walks free on time served.

## How to run

```sh
python3 main.py > news.jpg
```

The program only reads the bundled image and writes its bytes to stdout.
No network access, no randomness — running it twice produces identical bytes.

## Sources

- The Straits Times, "While You Were Sleeping", 24 November 2026
- Investopedia / Reuters / The Business Times, US market close 23 November 2026
- The Wall Street Journal, "How Epic Was Today's Stock Rally?"
- Channel News Asia / Reuters, Virginia and Oregon sue SpaceX over Grok, 24 November 2026
- The Japan Times / South China Morning Post, world headlines, 24 November 2026
