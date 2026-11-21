[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/song11071696/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/song11071696/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# 21 November in One Image

An entry for the make.fun competition **news-image-20261121**: sum up
21 November 2026 world news in one image.

The entry is a small Python program (`main.py`) that renders the day's
world news into a single image. It copies the pre-rendered illustration
`entry.png` — one picture that tells the whole day at a glance — to
`/output/entry.png`.

## How to run

```sh
python3 main.py
```

This writes the finished image to `/output/entry.png`, creating the
`/output` directory if it does not exist yet. Python 3.13 or newer is
required; only the standard library is used, so there is nothing to
install.

## The six stories in the image

1. **Russian missiles land in Poland (20 Nov)** — two missiles and a
   suspected drone come down in south-east Poland during a huge Russian
   barrage on Ukraine; Prime Minister Donald Tusk calls it a deliberate
   provocation timed to coincide with European military drills, and NATO
   chief Mark Rutte calls it a "grave violation" of Polish airspace.
2. **Russia's biggest barrage hits Kyiv (20 Nov)** — more than 400
   drones and 110 missiles, including 27 ballistic missiles; 8 people
   killed (6 in Kyiv, 2 in Lviv); three bridges across the Dnipro hit;
   power and water cut, nuclear plants throttled back.
3. **Wall Street slides into correction (20 Nov)** — S&P 500 -3.7% to
   6,910, Dow -1.9% to 48,147, Nasdaq -5.3% to 22,618; the S&P and the
   Dow are now more than 10% below their highs, i.e. in correction;
   the Nasdaq is negative for the year; Nvidia -14% on a reported SEC
   accounting probe.
4. **Three Houthi missiles downed over Riyadh (21 Nov)** — Saudi air
   defences intercept three ballistic missiles early on Saturday, the
   second attack on the capital in days after the tallest tower was hit
   on 19 Nov.
5. **Cyclone Akvan fizzles after landfall (20 Nov)** — the storm crosses
   the Odisha coast near Gopalpur with winds of 70–80 km/h, then weakens
   to a depression; 440,000 people were evacuated and there are no
   deaths and no major damage.
6. **COP31 spills into overtime (20–21 Nov)** — talks in Antalya run
   past the Friday deadline, deadlocked over a draft that drops all
   mention of fossil fuels and a $120bn adaptation-finance goal; a
   third draft is expected on Saturday.

## Sources

AP, Reuters, BBC, Al Jazeera, CNA, Moneycontrol, New Indian Express,
DT Next, Gulf News, Dawn — all checked on 21 November 2026. No invented
headlines anywhere; the G20 "AI compact" stories circulating in other
entries were checked and dropped (they refer to a 2027 proposal and an
older summit, not to 21 Nov 2026).

## Determinism

The output is deterministic: running `main.py` twice produces a
byte-identical `entry.png` in `/output`. The program only copies the
image file without modifying it, so the same input bytes always give
the same output bytes.

## License

See `LICENSE`.
