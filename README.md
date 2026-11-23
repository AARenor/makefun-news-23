[![make.fun news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/AARenor/makefun-news-23/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard)
[![reward](https://make.fun/badge/news-image-20261123/AARenor/makefun-news-23/reward.svg)](https://make.fun/bounty/news-image-20261123)

# World Briefing, Monday 23 November 2026

`entry.png` is a 1024 by 1024 newspaper front page for one day. It is drawn flat with Pillow by
`artwork.py`: a dark masthead with a wireframe globe, the words WORLD / BRIEFING and the date,
then six stories in two columns of three. Each card carries a section and source tag, a two line
headline in the serif face, a small drawn icon and one fact line. No photographs and no
gradients, and the page is built to stay legible at 300 pixels across.

## The six stories

1. **Ukraine.** Overnight Russian attacks on the Kyiv region killed at least 14 people. A strike
   on Dymer, about 45 km north of Kyiv, hit a five storey building and killed at least 11, and a
   strike on a supermarket in Vyshneve killed three and wounded 15, including three children.
   Nato allies were due to meet in Brussels on Monday over Russian Kh-101 missiles that fell in
   Poland.
   Source: [The Guardian](https://www.theguardian.com/world/2026/nov/23/ukraine-war-briefing-race-to-find-survivors-after-russian-attack-on-apartment-block-kills-at-least-nine), 23 November 2026.

2. **Libya.** President Volodymyr Zelensky said Ukrainian forces sank the Russian corvette
   Merkury, commissioned in 2023, near the coast of Libya using seven Ukrainian-made naval
   drones, and hit the Russian dry cargo ship MV Angara. The UN Support Mission in Libya called
   for an immediate, independent and transparent investigation.
   Source: [Arab News with Reuters](https://www.arabnews.com/middle-east/zelensky-confirms-ukrainian-army-targeted-russian-cruiser-in-libya-3013640), 23 November 2026, 00:43 UTC.

3. **Vanuatu.** A magnitude 6.5 earthquake in the Vanuatu region at 02:40 UTC, 598 km deep, at
   13.58 S 172.27 E. The USGS impact alert was green.
   Source: [USGS event us6000ucvm](https://earthquake.usgs.gov/earthquakes/eventpage/us6000ucvm), 23 November 2026, 02:40 UTC.

4. **Asia.** Seoul's Kospi slid as much as 5.8 percent before paring losses and was down 3.2
   percent at 04:30 GMT, while Hong Kong's Hang Seng and Shanghai's CSI 300 were each down about
   0.6 percent. Japan's markets were closed for Labour Thanksgiving Day. Wall Street's S&P 500
   had closed 3.7 percent lower on Friday, entering a correction, and the Nasdaq fell 5.3
   percent.
   Source: [Al Jazeera](https://www.aljazeera.com/news/2026/11/23/south-koreas-stock-market-tumbles-as-ai-bubble-fears-mount), 23 November 2026, 00:18 UTC.

5. **Gaza.** Oxfam and the Conflict and Environment Observatory reported that Israel's
   destruction of Gaza has left poisoned water, contaminated soil and toxic air, calling the
   contamination "widespread, severe and consequential". The UN Environment Programme estimates
   Israel's military operations have generated more than 61m tonnes of debris.
   Source: [The Guardian](https://www.theguardian.com/world/2026/nov/23/israel-gaza-destruction-created-toxic-wasteland-oxfam-report), 23 November 2026.

6. **Paris.** The Champs-Élysées Christmas illuminations were switched on, 400 trees and two
   million LEDs along the avenue, and the avenue's Christmas market returned after 10 years away
   with 200 exhibitors in wooden chalets between the Rond-Point and the Place de la Concorde.
   Cate Blanchett was the patron of the 2026 event.
   Source: [Euronews](https://fr.euronews.com/2026/11/23/les-champs-elysees-silluminent-pour-les-fetes-et-retrouvent-leur-marche-de-noel), 23 November 2026, 08:22 CET.

## Run

`python3 main.py` copies `entry.png` byte for byte into `out/entry.png` locally and into
`/output/entry.png` in the grader. The directory is chosen in this order: `--out DIR`,
`MAKEFUN_OUTPUT_DIR`, `OUTPUT_DIR`, `/output` when it exists, then `out/` beside the script. It
needs only the Python 3 standard library.

`artwork.py` is the offline design source and needs Pillow. Run `python3 artwork.py` to redraw
`entry.png`.

MIT license.
