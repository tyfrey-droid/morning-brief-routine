# Self-review log (internal — never published to Pages)

Bounded, best-effort notes the brief appends after each publish. No extra
searches or model calls — just a few honest lines to avoid repeating mistakes.
Read the last ~3 entries at the start of a run. See CLAUDE.md → "Self-evaluation".

Format per entry:
- **YYYY-MM-DD** — thin/empty sections & why · any story you were unsure cleared
  the bar · one concrete tweak to try next run.

---

- **2026-08-06** — Format change day: dropped One Good Thing + On This Day,
  moved to a Mon/Wed/Fri cadence, added per-story feedback flags. Mito Research
  omitted (24 in-window PubMed hits, none cleared the strict bar). EV ran a
  single strong item (Kia PV5) — fine, not padded. Next run (first Mon/Wed/Fri
  issue): use the "since last brief" lookback, and check open `brief-feedback`
  issues before selecting stories.

- **2026-08-06 (evening, off-cadence manual run)** — First test of the manual
  override; gate correctly bypassed on an explicit in-session ask. Lookback was
  only ~12h, so Sports/Kauai/Gear ran the "nothing new" line and World carried a
  single item — thin by design, not padded. Missed the Aug 5 Kyiv barrage (17
  killed, zero ballistic intercepts) in the morning edition despite strong wire
  consensus; caught it here. Tweak next run: in the World/US consensus sweep,
  explicitly check the Ukraine/Russia thread each cycle — it was crowded out by
  FIFA and Israel–Lebanon this morning.

- **2026-08-11 (off-cadence Tue, manual "fix it" run)** — OUTAGE FIXED. Nothing
  had published since Aug 6: the external trigger fires on UTC weekdays (~04:10
  UTC Mon/Wed/Fri), landing ~9 PM PT the *evening before* each intended publish
  day — always an off-cadence Pacific day — so the cadence gate stopped every
  firing and no brief shipped for ~5 days while fetch-conditions.yml kept
  refreshing data for briefs that never came. Added a UTC-skew guard to CLAUDE.md
  so a gated firing on the eve of a publish day now publishes instead of dying
  silently (with a same-day dedupe check). Real fix still pending: the owner must
  reset the trigger to ~6 AM America/Los_Angeles. This issue: World ran a full 3
  (Ukraine deep strikes, Netanyahu–Trump split, Hormuz terms), Sports a healthy 3
  (Moda Center county vote, Warriors schedule, Don Nelson obit). Thin by honest
  design: San Diego 1 (no 2nd item cleared the ≤14-day bar — pro/local sites
  egress-blocked), Gear 1 (DJI Osmo Pocket 4P; pro-video anchors all blocked),
  EV 1 (ID. Buzz). Mito omitted — PubMed 28-hit window, nothing cleared the
  strict bar (closest: MTERF1 bioRxiv preprint on mtDNA *deletions*, not
  m.3243A>G; and a Newcastle digital-cognition methodology paper). Tweak next
  run: confirm firings have moved into the 5–7:30 AM PT window; if still skewed,
  keep flagging in the report.

- **2026-08-13 (Thu evening, UTC-skew guard fired — first automatic use)** — The
  guard added on Aug 11 worked exactly as designed: firing landed 9:20 PM PT
  Thursday (off-cadence Pacific day) but Friday UTC, i.e. the eve of a publish
  day, so the gate was bypassed and the brief published instead of dying. Dated
  with the actual Pacific date per CLAUDE.md; weather rows were framed
  TONIGHT / FRIDAY / SATURDAY so a Thursday-dated, Friday-read issue stays
  internally coherent — worth keeping as the pattern for early firings.
  **The trigger is STILL misconfigured** (~04:10 UTC Mon/Wed/Fri); the owner
  must move it to ~6:00 AM America/Los_Angeles. Counts: World 3, US 3, Tech 2,
  Sports 2, San Diego 2, Kauaʻi 1, Gear 1, EV 1. Mito omitted again — PubMed
  returned 316 hits in the window but nothing cleared the strict bar; the two
  near-misses were a MELAS pulmonary-hypertension case report (excluded: case
  report, no new mechanism) and a strong urinary-heteroplasmy screening paper in
  Mol Genet Metab that would have qualified except it published Jun 26, outside
  the 14-day window. Dropped a Padres wild-card bullet because the only MLB.com
  article surfaced had no confirmable publish date. Tweak next run: pro-video
  and local-news anchors are still egress-blocked, so gear/San Diego depend
  entirely on search phrasing — lead those searches with a dated outlet query
  ("newsshooter.com August 2026") which is what finally surfaced the one gear item.

- **2026-08-16 (Sun evening, UTC-skew guard fired — second automatic use)** — Guard
  worked again: firing at 9:15 PM PT Sunday (off-cadence Pacific) but Monday UTC,
  i.e. the eve of a publish day, so the gate was bypassed. Dated with the actual
  Pacific date; weather rows framed TONIGHT / MONDAY / TUESDAY per the Aug 13
  pattern. **Trigger is STILL misconfigured** (~04:10 UTC Mon/Wed/Fri) — owner must
  move it to ~6:00 AM America/Los_Angeles. Counts: World 3, US 2, Tech 2, Sports 1
  (+ an honest "NBA dead stretch" line), San Diego 2, Kauaʻi 2, Gear 1, EV 1, Mito 1.
  Unsure calls: (a) included the lamotrigine/Stevens-Johnson case report in Mito —
  the filter says exclude case reports, but it proposes a mechanism AND is a drug
  safety signal in seizure management for mito patients, which the INCLUDE list
  names explicitly; framed it hard as hypothesis-generating, N=1. (b) EV ran the
  Lucid Gravity GT-S, a $127k three-row — family *format*, not family *price*; said
  so in the bullet rather than pretending otherwise. Excluded despite consensus:
  Hormuz Iran–Oman shipping-map deal (third consecutive brief; Araghchi conceded it
  does not reopen the strait, so the new development was thin). Date-excluded: Ja
  Morant→Blazers trade (Jun 29), Sony FX5 (Jul 22). Egress blocked newsshooter.com,
  insideevs.com, macrumors.com, provideocoalition.com, espn.com this run — search
  snippets carried the load. Tweak next run: NBA is dead until camps open in late
  Sept, so plan on Padres/MLB carrying Sports for the next several issues rather
  than re-running the "nothing new" line each time.

- **2026-08-18 (Tue evening, UTC-skew guard fired — third automatic use)** — Guard
  worked again: firing at 9:08 PM PT Tuesday (off-cadence Pacific) but Wednesday
  UTC, i.e. the eve of a publish day, so the gate was bypassed. Dated with the
  actual Pacific date; weather rows framed TONIGHT / WEDNESDAY / THURSDAY per the
  Aug 13 pattern. **Trigger is STILL misconfigured** (~04:10 UTC Mon/Wed/Fri) —
  owner must move it to ~6:00 AM America/Los_Angeles. Counts: World 3, US 2,
  Tech 2, Sports 2 (+ NBA dead-stretch line), San Diego 3, Kauaʻi 1, Gear 1,
  EV 1, Mito 1. Unsure calls: (a) Mito ran the Turku drug-safety cohort (Neurol
  Sci, Aug 6) one brief after the Aug 16 lamotrigine case report — thematically
  adjacent, but a distinct study with real cohort data and a named drug list, so
  it clears "new safety data"; watch for a third drug-safety item in a row and
  drop it if so. (b) Padres appeared in both Sports (sale, wild card) and San
  Diego (ICE detains a coach) — three Padres bullets is a lot, but the $3.9B sale
  and an ICE arrest are genuinely different stories. Excluded despite consensus:
  Ukraine deep-strike drone attacks (third brief running, nothing new beyond the
  pattern); Kushner–Hamas Cairo talks (ran Aug 16); Virginia State University
  shooting (Aug 15, predates the lookback and had faded by Tuesday). Date-excluded:
  Trump "master list of espionage targets" (underlying reporting traces to early
  July); MELAS pulmonary-hypertension case report (already excluded Aug 13).
  Egress blocked this run: reuters.com, apnews.com, bbc.com, pbs.org, npr.org,
  democracynow.org, kpbs.org, thegardenisland.com, cined.com, newsshooter.com,
  xdcam-user.com, thepourover.org — so no TPO cross-check was possible and Gear
  again rested entirely on a search-surfaced PetaPixel item. WebSearch also now
  rejects allowed_domains lists containing reuters/ap/bbc/verge/arstechnica —
  don't waste calls on domain-filtered searches; use plain queries and filter the
  returned URLs by hand. Tweak next run: the single most productive query shape
  was "<outlet> news <exact date>" (e.g. "Padres news August 18 2026"), which is
  what surfaced the KPBS ICE story and the whole San Diego section — lead with
  that for local and niche sections instead of topic-only queries.

- **2026-08-20 (Thu evening, UTC-skew guard fired — fourth automatic use)** — Firing at
  9:09 PM PT Thursday (off-cadence Pacific) but Friday UTC, i.e. the eve of a publish
  day, so the gate was bypassed and the issue dated with the actual Pacific date.
  **Trigger is STILL misconfigured** (~04:10 UTC Mon/Wed/Fri) — owner must move it to
  ~6:00 AM America/Los_Angeles; four consecutive off-slot publishes now. Counts:
  World 3, US 2, Tech 3, Sports 2, San Diego 3, Kauaʻi 2, Gear 1, EV 1, Mito 0
  (omitted). (a) Thin/empty: Gear ran a single item and it is a consumer pocket gimbal,
  not FX6-adjacent — the only pro-video item in window was the FX5 delay, already run
  Aug 18 with no new development, so I took the Insta360 launch and said plainly in the
  bullet that it does not touch an FX6 rig. EV ran one item for the same reason: the
  Rivian AWD/big-battery story traces to a February shareholder letter and the
  Amazon-fleet update to ~Aug 5, both outside 14 days. Mito omitted — both PubMed hits
  (Biomed Pharmacother 10.1016/j.biopha.2026.119699, Mol Neurobiol
  10.1007/s12035-026-06008-2) are 2026-06-26 reviews, date-excluded, and the second
  fails the review exception anyway. (b) Unsure call: the Darth Vader/Flock item is a
  stunt, but it is the visible edge of a real surveillance-policy fight and both The
  Hill and 404 Media covered it — kept it third in the section, not first. (c) Excluded
  despite consensus: Lavrov's warning that UK-made drones make Britain a party to the
  Ukraine war — the sourcing available to me was the paywalled Times original plus RT
  (Russian state media) and aggregators, and Ukraine ran in the last two briefs.
  Egress blocked this run: justsecurity.org, timesofsandiego.com, 9to5mac.com,
  newsshooter.com, cined.com, 10news.com. Tweak next run: for Gear, search the product
  category rather than the outlet ("cinema camera announced <date>", "Sony E-mount
  <date>") — outlet-name queries kept returning site landing pages, while the one item
  that surfaced came from a product-name query.

- **2026-08-23 (Sun evening, UTC-skew guard fired — fifth automatic use)** — Firing at
  9:09 PM PT Sunday (off-cadence Pacific) but Monday UTC, the eve of a publish day, so
  the gate was bypassed and the issue dated with the actual Pacific date. Newest archive
  was 2026-08-20, so the dedupe guard did not trip. **Trigger is STILL misconfigured**
  (~04:10 UTC Mon/Wed/Fri) — the owner must move it to ~6:00 AM America/Los_Angeles;
  five consecutive off-slot publishes now. Counts: World 3, US 3, Tech 3, Sports 3,
  San Diego 3, Kauaʻi 2, Gear 1, EV 1, Mito 1. (a) Thin: Gear again ran one item — the
  FoMa Maxima Mk II remote head — and I said in the bullet that it does not bolt to an
  FX6, because the only FX6-specific gear in reach (Bright Tangerine monitor hinge,
  SmallRig FX6 cage) is from June and date-excluded. EV had nothing on vans or family
  formats at all, so the Nevada robotaxi approval ran as the single "(general EV news)"
  item. (b) Unsure call: the Mito item is a review, and reviews normally fail the bar.
  I kept it because it clears the review exception on specifics — idebenone/EMA 2015,
  Friedreich's 2023, FDA 2025 for Barth and TK2d, with gene and nucleoside therapy named
  as the approaches that worked — and I led with those and stated plainly that none of
  them touches m.3243A>G. If the reader flags it as not actionable, tighten the exception
  to require a MELAS-relevant agent. (c) Also excluded despite consensus: AAA's record
  gas price ($4.10, highest ever for Aug. 20) — genuinely water-cooler, but the only
  citable source I could reach was AAA's own newsroom, and the World/US selection rule
  needs two outlets. Egress blocked this run: apnews.com, reuters.com, bbc.com, npr.org,
  cnn.com, espn.com, electrek.co, newsshooter.com, cined.com, ymcinema.com, kpbs.org,
  thepourover.org — every direct fetch failed, so the whole run was web-search-only.
  Tweak next run: TPO could not be fetched or found via search, so the water-cooler gate
  ran on consensus alone; try searching "the pour over" plus a story keyword rather than
  the site, or drop the TPO cross-check from the report when it is unreachable instead of
  leaving the column blank.

- **2026-08-25 (Tue evening, UTC-skew guard fired — sixth automatic use)** — Firing at
  9:11 PM PT Tuesday (off-cadence Pacific) but Wednesday UTC, the eve of a publish day,
  so the gate was bypassed and the issue dated with the actual Pacific date. Newest
  archive was 2026-08-23, so the dedupe guard did not trip. **Trigger is STILL
  misconfigured** (~04:10 UTC Mon/Wed/Fri) — the owner must move it to ~6:00 AM
  America/Los_Angeles; six consecutive off-slot publishes now. Counts: World 3, US 3,
  Tech 3, Sports 3 (one a no-development note), San Diego 2, Kauaʻi 1, Gear 1, EV 1,
  Mito 0 (section omitted). (a) Thin: Gear ran one item and it is a research paper, not
  a product — every reachable pro-video release (Laowa Aksen Aug 3, Saramonic K9 XTX
  Aug 6) fell outside the 14-day bar, and cined.com, newsshooter.com and ymcinema.com
  were all egress-blocked so I could only work from search summaries. EV also ran one:
  no van or family-format release cleared the window, so the PG&E V2X expansion carried
  the section on the strength of the EV9/EX90/Bolt eligibility list, flagged as PG&E
  territory rather than SDG&E. Mito omitted correctly — the only PubMed hit inside 14
  days was the Karaa scoping review already run on Aug 23; everything else (riboflavin
  Jul 13, SPP-004 Leigh Phase III Jul 17, POLG nucleoside Jun 15) is date-excluded.
  (b) Unsure call: the Apple event bullet is Gurman reporting, not an announcement, and
  normally that is a weak item — I kept it because the reader is Apple-priority and
  labeled it plainly as reporting in the bullet itself. Also unsure: the Padres line is
  a stated non-development rather than a story; if that reads as filler, drop the line
  entirely next time instead of announcing the absence. (c) Excluded despite consensus:
  the Senate/House stopgap funding deal through Dec. 11 leads widely but dates to Aug. 8,
  outside the 14-day bar as a new development. Egress blocked this run: npr.org,
  axios.com, espn.com, insideevs.com, cined.com, ymcinema.com, justsecurity.org,
  thepourover.org — search-only again, and TPO was unreachable for the fourth straight
  run. Tweak next run: stop attempting the TPO cross-check and drop its column from the
  consensus table until the block lifts; the WORLD Radio daily rundown surfaced the same
  water-cooler set (Canada tariffs, Iran sanctions) and is reachable, so use it as the
  visibility signal instead.

- **2026-08-27 (Thu evening, UTC-skew guard fired — seventh automatic use)** — Firing at
  9:09 PM PT Thursday (off-cadence Pacific) but Friday UTC, the eve of a publish day, so
  the gate was bypassed and the issue dated with the actual Pacific date. Newest archive
  was 2026-08-25, so the dedupe guard did not trip. **Trigger is STILL misconfigured**
  (~04:10 UTC Mon/Wed/Fri) — the owner must move it to ~6:00 AM America/Los_Angeles;
  seven consecutive off-slot publishes now. Counts: World 3, US 3, Tech 4, Sports 2,
  San Diego 3, Kauaʻi 1, Gear 1, EV 1, Mito 2. (a) Thin: Gear ran one item again — the
  GoPro MISSION 1 PRO ILS was the only pro-video release inside 14 days that I could
  reach; the Blackmagic URSA Cine Immersive 100G and Cartoni/Ikegami IBC items all date
  to NAB (April) or Aug. 4 and were date-excluded, and cined.com, newsshooter.com,
  ibc.org and gopro.com were egress-blocked so the bullet is built from PetaPixel plus
  the PR Newswire release. EV also ran one: no van or family-format story cleared the
  window (the VW ID. Buzz and Kia PV5 hits were all months old), and the MyFirstEV/Tesla
  rebate item that search surfaced was already run Aug. 13, so the Electrek FSD
  railroad-crossing report carried the section as flagged general EV news.
  (b) Unsure call: the second Mito item is a narrative review, and the Aug. 23 brief
  already ran a horizon-scan review — I kept it only because sonlicromanol/KHENERFIN and
  KL1333/FALCON appear in no prior brief (grep-checked), and I led with those rather than
  with taurine, which ran June 29. If the reader flags it as redundant, the rule to adopt
  is one review per month regardless of new named trials. Also unsure: the Kuminga bullet
  is league-wide rather than Blazers/Warriors — he is a *former* Warrior traded to Atlanta
  in February, so the team hook is thin; I folded the "nothing new from Portland or Golden
  State" note into that bullet instead of running it as its own line, per the Aug. 25
  tweak. (c) Excluded despite consensus: the WHO Ebola announcement (Uganda outbreak over,
  DRC ongoing) led on several outlets but I could not reach a wire page to verify the
  framing, so it was dropped rather than summarized from aggregated search text.
  Egress blocked this run: npr.org, aljazeera.com, kpbs.org, electrek.co, insideevs.com,
  cined.com, newsshooter.com, ibc.org, gopro.com — search-only again. Per the Aug. 25
  tweak I did not attempt thepourover.org and dropped its column from the consensus table.
  Tweak next run: the anti-redundancy grep against archive/ caught two would-be repeats
  (MyFirstEV, taurine) before drafting — run that grep on every candidate headline's key
  proper nouns *before* writing the section, not after, and budget the time saved toward
  a second reachable Gear source.

## 2026-08-30 (published early for the Mon Aug 31 slot)
(a) Thin/empty: 🧬 Mito omitted entirely — the only qualifying-looking hit was another MELAS
  narrative review (PMID 42644018, Aug 31) naming taurine, sonlicromanol/KHENERFIN, zagociguat,
  TTI-0102 and KL1333/FALCON, i.e. the same therapeutic movement the Aug 27 brief already ran;
  I applied the "one review per month" rule the Aug 27 entry proposed and dropped it. The rest of
  the window was case reports (Turner-masked MELAS, m.3303C>T family) and off-target mtDNA papers.
  🎥 Gear ran empty for real: the trade press sits between NAB and IBC (opens Sept 11), and the
  Sony FE 100-400mm (Aug 4) and FX5 delay (ran Aug 18) are both outside the window. 🌺 Kauai empty —
  the mayoral race is between the Aug 8 primary and the Nov 3 general.
(b) Unsure calls: Dolly Parton. She died Aug 25 and no prior brief covered it — a genuine miss,
  not a redundancy question — so I ran it in US & Politics led on the weekend burial rather than
  on the death, which is 5 days old. Placement is imperfect (there is no culture section) but it
  was the week's clear water-cooler story. Also unsure: two Anthropic items in one Tech section.
  They are unrelated (the Pentagon supply-chain ruling; the 35-publisher copyright suit) and both
  were top-of-section news, so I kept both and wrote them straight.
(c) Tweak next run: the Aug 27 tweak — grep archive/ for each candidate's proper nouns BEFORE
  drafting — worked and caught four would-be repeats (Niang, EV9/PG&E, FX5 delay, the ID.
  California Cruise *preview*, which I reframed around Friday's actual reveal specs rather than
  dropping). Keep it. New tweak: also grep for names that are absent, not just present — Parton
  returned zero hits across every archive, which is what surfaced the miss. Run a
  "biggest-story-of-the-week absent from archive/" check each Monday.
Egress blocked this run: npr.org, pbs.org, axios.com, cbsnews.com, cnn.com, kyivindependent.com,
usnews.com, timesofsandiego.com, cbs8.com, kauainownews.com, xdcam-user.com — search-only again;
links are cited to the outlets that reported the story, dates verified from search result metadata
and URL date paths.

## 2026-09-02 (Wednesday — first firing on the correct Pacific day since the schedule reset)
(a) Thin/empty: 🎥 Gear ran one item and it is a patent, not a product — the trade press is still in
  the NAB/IBC gap (IBC opens Sept. 11) and nothing shipped in the window. 🌺 Kauai ran one (Section 8
  waiting list) with a Garden Island briefs page as the best available link; the mayoral race is still
  between the primary and the Nov. 3 general. 🌊 San Diego ran two, not three: I drafted a third on the
  city's $15M affordable-housing round and cut it at the last check because the search results mixed a
  July NOFA, an April 6 application deadline and a Sept. 1 post, and I could not pin the publication
  date inside 14 days. Dropping it was right, but I should have date-checked before drafting.
(b) Unsure calls: the OpenAI "Jalapeño" chip is from Aug. 25 — inside the 14-day window but outside the
  since-Aug-30 lookback, and no prior brief covered it, so I ran it as a miss-catch rather than a fresh
  item. Same logic for Norway (Harald V died Aug. 28, uncovered) and Venezuela (announced Aug. 28), both
  led on what happened since: the Storting oath Tuesday, and the deal's actual ownership structure.
  Also unsure: the second Mito item is a diabetes registry study and the daughter is 7 with onset
  clustering near 48. I kept it because it answers the metformin caution the Aug. 18 brief raised, with
  m.3243A>G-specific data rather than a general warning — that is new information on a named drug, not
  a prevalence count. The Warriors bullet is thin (an Exhibit 10 deal) and sits close to Aug. 30's
  "offseason has gone quiet"; I ran it only because Portland has nothing and the section would otherwise
  have no NBA at all.
(c) Tweak next run: the Aug. 30 tweak — grep archive/ for candidate proper nouns before drafting — again
  earned its keep (caught the Apple Sept. 9 event, the Kia EV9 recall flavor, taurine/sonlicromanol) and
  the absent-name check surfaced Norway and Venezuela the same way it surfaced Parton. Keep both. New
  tweak: date-verify BEFORE writing the bullet, not after. I wrote the San Diego housing item in full
  and then threw it away; that is the same wasted pass the anti-redundancy grep was moved earlier to
  avoid. Also: when assembling from a prior archive as a template, diff the assembled file against the
  template tail — the Aug. 30 closing quote survived outside </main> and shipped in the first commit
  before I caught it on a full read. Add a "exactly one <blockquote>" assertion to the build step.
Egress blocked this run: reuters.com, apnews.com, bbc.com, macrumors.com, timesofsandiego.com,
newsshooter.com, insideevs.com, thegardenisland.com — search-only again; every link's publication date
was verified from search result metadata and URL date paths. Per the Aug. 25 tweak I did not attempt
thepourover.org and dropped its column from the consensus table.
