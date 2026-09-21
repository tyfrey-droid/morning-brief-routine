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

## 2026-09-04 (Friday — on-cadence, scheduler fired 5:38 AM PT)
(a) Thin/empty: 🌺 Kauai ran the "nothing significant" line — The Garden Island's only in-window items
  were a Labor Day breakfast, a Kalalau Trail ankle rescue and a Sept. 19 health fair; nothing cleared the
  bar and the mayoral race is still idle between primary and Nov. 3. 🎥 Gear ran one item (DJI Osmo 360 II)
  and it is a consumer 360 camera, not pro video — the trade press is still in the IBC gap (opens Sept. 11),
  exactly as predicted Sept. 2. I framed it honestly rather than pretending it was an FX6-adjacent release.
  🧬 Mito ran one. US & Politics ran two, not three: I looked at the House court-packing amendment vote
  (212–206, failed) but could not pin it to a reputable outlet with a verifiable date, so I dropped it before
  drafting — the Sept. 2 tweak working as intended.
(b) Unsure calls: the Mito item (VISTA / FnCas12a lateral-flow readout for m.3243A>G, Anal Chem Aug. 25) is a
  methods paper, not a therapy, and I nearly cut it. Kept it because it is a diagnostic advance at her exact
  variant with clinical-sample validation, and wrote the four real limits into the bullet rather than
  overselling it. I deliberately EXCLUDED the Aug. 31 MELAS review (Intractable Rare Dis Res) even though it
  is the most on-topic paper in the window — its specifics (taurine approval, sonlicromanol KHENERFIN,
  zagociguat, KL1333/FALCON) were all covered Aug. 27 and earlier, so under the review-article exception it
  surfaces nothing new. Also excluded the PNAS scMPCDS single-cell paper: that IS the Sept. 2 item.
  Second unsure call: the Sharpe injury is Aug. 26–27, inside 14 days but well outside the since-Sept-2
  lookback. Ran it as a miss-catch — Aug. 30 said "the offseason has gone quiet" without ever naming it,
  and it is the biggest Blazers story of the month.
(c) Structural note worth keeping: the Iran story was the obvious World lead, but the Sept. 2 archive already
  carried the Jordan interception with the identical 10-of-13 detail. Rather than re-summarise it, I moved
  the thread to US & Politics framed on what is actually new — Vance's "I wouldn't call it a war," the
  war-powers votes, and the Klinner widow's withheld combat pay — and left World to four genuinely fresh
  stories. Generalize this: when a running story has no new *event*, check whether it has a new *frame* in
  another section before dropping or repeating it.
(d) Tweak next run: I could not verify a verbatim John Swinton quote (goodreads, abdn.ac.uk both egress-blocked)
  even though he was the correct rotation slot at 15 days. Rather than fabricate one I fell back to Augustine
  (Confessions IV.9, distinct from the Aug. 11 and Aug. 25 quotes). Fix: keep a small verified quote bank in
  this repo so rotation never depends on live egress. Start it next run with 3–4 Swinton lines sourced when
  a fetch succeeds.
Date-excluded this run: De Anza Natural / ReWild Coastal Commission approval — Times of San Diego published
Aug. 31 but the vote itself was Aug. 14, and the older-date rule puts it outside 14 days. Kia PV7 electric van
(IAA debut Sept. 14) excluded as redundant: Sept. 2 already ran "Kia previews a bigger electric van."
Egress blocked this run: openai.com, 9to5mac.com, thehackernews.com, goodreads.com, abdn.ac.uk; and reuters.com,
apnews.com, theverge.com, arstechnica.com, wired.com, ft.com, zdnet.com, theguardian.com, sandiegouniontribune.com
are refused to the search user-agent. Search-only again; every link's date verified from result metadata and URL
date paths. Per the Aug. 25 tweak I did not attempt thepourover.org and dropped its column from the consensus table.

## 2026-09-07 (Monday, Labor Day)
(a) Thin/empty sections: 🧬 Mito omitted entirely — the Aug 24–Sep 7 PubMed window returned 50 hits and none
  cleared the bar. The two closest were already covered: PNAS scMPCDS (PMID 42673453) ran Sept. 2, and the
  GENOMIT mitochondrial-diabetes/metformin registry paper (PMID 42679752) is the Sept. 2 metformin item. The
  rest were reviews (Alzheimer's mito, CLPP), case reports (MELAS masked by Turner syndrome; MT-ND4 anaesthesia
  encephalopathy), the UMDF TK2d masterclass write-up (explicit "multidisciplinary care" exclusion), or
  off-target. 🏀 Sports ran a single bullet: NBA offseason is genuinely quiet and Sharpe/Moda Center were both
  spent on Sept. 4. 🔋 EV ran one — no van or family-format story existed in the window, so one general filler
  per the CHANGE 3 cap.
(b) Unsure calls: I dropped the Blazers' Sept. 7 Exhibit 10 signing (Lee Hyun-jung). It is Blazers-first and
  dated today, but an unguaranteed camp contract is exactly the padding the filter exists to stop, and Sept. 2
  already ran "Golden State adds a camp body" — running the same non-story for the other team two briefs later
  would be redundancy in spirit if not in letter. Also dropped Brandon Williams to Golden State (Aug. 25):
  inside 14 days but outside the since-Sept-4 lookback, and I could not rule out that it WAS the Sept. 2
  "camp body" bullet. Second unsure call: the Poway school-bus lawsuit is Aug. 30, outside the lookback, run
  as a deliberate miss-catch — neither Sept. 2 nor Sept. 4 carried it and it is a substantial local story.
(c) Process note: I nearly shipped with a stale <title> ("Friday, September 4"). The head/CSS is spliced
  verbatim from the previous index.html, and the masthead .date and the <footer> both get rewritten in the
  body block while the <title> lives up in the head — so it is the one date the body rewrite never touches.
  Caught it on the post-assembly read, but only by luck. Generalize: after assembly, grep for the PREVIOUS
  brief's date string across the whole file, not just eyeball the masthead.
(d) Tweak next run: the quote bank idea from Sept. 4 is still unbuilt and it bit again. Swinton was the right
  rotation slot (18 days, and the correct author for this reader), but the only Swinton line I could verify
  live — "God's time is slow, patient, and kind" — is the Aug. 20 quote, inside the 30-day no-repeat window,
  and I would not ship the "embodied theodicy of practice" line because I could not confirm it was verbatim
  Swinton rather than a reviewer's paraphrase. Fell back to MLK ("unearned suffering is redemptive," Suffering
  and Faith, 1960; Aug. 23's MLK quote was a different one). Actually build the bank next run: 3–4 verified
  Swinton lines with book and page, committed to this repo, so rotation stops depending on live search.
Date-excluded this run: the "Pacing the Frontier" AI-employee petition — surfaced via a Sept. 6 CNBC piece but
the letter itself is July 28, well outside 14 days, so the underlying event fails the older-date rule. The
Aug. 31 MELAS review (Intractable Rare Dis Res) remains excluded for the second run running — same specifics
(taurine, sonlicromanol/KHENERFIN, zagociguat, KL1333/FALCON) as Aug. 27 and earlier.
Source note: avoided the abcnews.com URLs that search kept returning for ABC News stories — ABC's real domain
is abcnews.go.com, and under the "displayed name must match the linked domain" rule I would not cite a domain
I could not confirm. Used NBC News/SCOTUSblog and NPR/WaPo/CBS for those two stories instead.

## 2026-09-09 (Wednesday)
(a) Thin/empty sections: 🌍 World ran 2, not 3 — the West Bank trade measures and Canada's
  counter-tariffs both cleared the multi-outlet bar cleanly, but the third candidates (Kenya's
  crackdown on foreign small-business owners, the UNGA world-map vote) each surfaced in exactly one
  search summary and no second outlet, so they failed the 2-outlet rule rather than the interest
  test. 🏀 Sports ran one real bullet plus an explicit "nothing moved" line: Portland and Golden
  State have genuinely done nothing since the Sharpe diagnosis on Sept. 4, and the US Open final is
  not until Sept. 13. 🔋 EV had exactly one van story (ID. Buzz Cargo LWB) and one general item —
  correct under the CHANGE 3 cap, not padding. 🌺 Kauai ran one, which is the ceiling that matters
  here anyway.
(b) Unsure calls: two. First, the L-arginine paper is a systematic review, which the Mito filter
  excludes by default. I ran it under the review exception because it is a quantitative synthesis
  producing pooled effect sizes on a named drug the reader's daughter plausibly takes, not a
  narrative "more research needed" — but it is the closest call the section has had. Second, the
  Apple bullet: the Sept. 7 brief already covered the event, and "the event is today" is not a new
  development. I framed it strictly around the release calendar (pre-orders Sept. 12, on sale
  Sept. 18, shifted off the Sept. 11 anniversary), which genuinely firmed up Sept. 6. Defensible,
  but if the next run finds itself doing this again it should just drop Apple for the cycle.
(c) Process: the Sept. 7 note about grepping for the PREVIOUS brief's date after assembly worked —
  ran it, the only hit was "September 2036" inside the Qualcomm warrant text, a false positive.
  Keep the check; expect that class of false positive. Second catch: I wrote the EV tag as
  <span class="tag">, a class that does not exist in the stylesheet. Caught it by grepping every
  class I used against the CSS before committing. Make that grep standard too — the head/CSS is
  spliced verbatim from the prior file, so any NEW class name in the body is silently unstyled.
(d) Tweak next run: the Drive upload is the single most expensive step in the run — ~35KB of HTML
  retyped into a tool call. This run cut it in half by uploading once to Archive and then using
  Drive's copy_file to place "Current Brief.html" in the folder root. Do that every time; do not
  upload the same document twice.
Date-excluded this run: nothing new was cut on date grounds. Mito exclusions were relevance, not
date — the TK2d/UMDF masterclass write-up (explicit multidisciplinary-care exclusion, and already
excluded once), the Turner-syndrome MELAS case report (no new mechanism), the Alzheimer and
preterm-brain-injury mitochondrial reviews (off-target), the CML mtDNA paper (oncology), and the
Intractable Rare Dis Res MELAS review, now excluded for a third consecutive run.
Source note: The Pour Over's latest issue at run time was "Fully Reignited," roughly Sept. 4 —
entirely inside the previous brief's window, so it offered no cross-check signal on this run's
World/US picks. That is the failure mode the routine already warns about (they publish 3x/week);
on a Wednesday run their latest issue will usually be stale. Treat a Wednesday TPO check as
optional rather than spending a fetch on it.
Quote: built QUOTES.md this run, per the standing note from Sept. 4 and Sept. 7. Swinton was the
correct rotation slot again (20 days) and failed verification again for the third run — the only
lines I can surface live are publisher framing questions and a reviewer's "embodied theodicy of
practice," neither confirmable as verbatim. Went to Bonhoeffer (13 days, different quote and
different letter) with the Christmas Eve 1943 letter to Renate and Eberhard Bethge, which is
verifiable. Swinton stays unverifiable until someone checks a physical copy; QUOTES.md now records
that explicitly so the next run stops re-litigating it.

## 2026-09-11 (Friday)
(a) Thin/empty: 🎒 School omitted entirely — the only qualifying-window mail was Back-to-School
  Night (already carried Sept. 9, and it happened Sept. 10), spirit-wear marketing, a same-day
  volunteer ask that had expired by publish, and a private one-to-one teacher exchange that the
  privacy rule excludes outright. MAP testing Sept. 14–16 was tempting as "now imminent," but it
  ran one brief ago unchanged, so restating it would have been padding. US & Politics ran 2 of a
  possible 4: the convention and the Missouri ruling were the only stories clearing the 2-outlet
  consensus bar with a genuine development. EV ran 2 by design. Kauai 1.
(b) Unsure it cleared the bar: the Mito item. The GENOMIT finding is adult-onset diabetes, not
  childhood MELAS, which is a real distance from this reader's situation. It got in because it is
  genotype-specific to m.3243A>G (HR 10.3), names a drug (metformin), and replaces mechanism-based
  caution with registry data — the review-exception test. Flagged that distance in the bullet
  rather than overselling it. Also borderline: Patch Tuesday, which is Sept. 8 and so predates the
  last brief by a day, but was never covered and has a Sept. 22 CISA deadline attached.
(c) Process: the class-name grep and the previous-brief-date grep both ran clean (the only 09/09
  hits were legitimate article URLs). Domain-vs-display-name audit caught one real error — I had
  labelled a doi.org link "EBioMedicine". Make that audit standard; it is the one check that has
  now caught something twice. Egress blocking was much worse this run: apnews.com, bbc.com,
  macrumors.com, appleinsider.com, thepourover.org and api-docs.deepseek.com all refused. Search
  with allowed_domains was the workaround, but note reuters.com, theguardian.com, nytimes.com,
  wsj.com, politico.com and theverge.com are all rejected by the search API's user agent — do not
  waste calls putting them in allowed_domains.
(d) Tweak next run: I dropped a DeepSeek V4.1-Flash item because every source search surfaced was
  a content farm and the primary changelog was egress-blocked. That was the right call, but it
  cost two searches to reach. Next time a story only surfaces on aggregator/SEO domains, drop it
  on the first pass instead of hunting for a reputable second source.
Date-excluded this run: Canon CINE-SERVO 40-1200mm (announced Apr. 15 at NAB, ships this month —
the ship date is not a publication date); Warriors' Niang/Williams signings (August, and the
Sept. 9 brief's "offseason stays quiet" was correct); Warriors Hawaii camp announcement itself is
Aug. 31, cited only as a forward-looking date. Mito exclusions were relevance, not date: the ND6
allotopic-expression paper (covered Sept. 9), the VISTA FnCas12a assay (covered Sept. 4), the TK2d
masterclass (fourth consecutive exclusion), the Turner/MELAS case report (second exclusion), the
endothelial-coupling and CLPP reviews, the vitamin/cofactor prescribing-patterns paper, and the
CHOP contrast-enhanced-ultrasound study — the last of which is genuinely interesting but is 5 vs 5
with no significant between-group result.
Source note: The Pour Over is now egress-blocked outright (thepourover.org, EGRESS_BLOCKED), not
merely stale. The water-cooler gate ran on wire/public-broadcaster consensus alone. If the block
persists, the routine's TPO cross-check step should be rewritten or dropped rather than retried
every run.
Quote: Swinton was oldest in rotation (22 days) and remains unverifiable per QUOTES.md, so fell
through to Keller (12 days), different book from his last appearance — The Meaning of Marriage,
the "fully known and truly loved" passage. Verified as widely and consistently attributed.

## 2026-09-14 (Monday)
(a) Thin/empty: 🇺🇸 US ran 2 (the Missouri map and mail-ballot stories were both covered Sept. 7/11
  with no new development since). 🌊 San Diego ran 2 — the county Medicaid vote was Sept. 3 and
  already carried Sept. 4, the Haitian-community ICE protest overlapped Sept. 11's City College
  protest bullet, and the Padres-ownership item KPBS surfaced turned out to be Aug. 24. 🌺 Kauai
  ran 1, correctly — restoration is now an incremental percentage story. ⚓ GW watch produced
  NOTHING and that is the right output: the newest USNI Fleet Tracker is Sept. 8, predating the
  last brief, and no position change, incident or claim has surfaced since. Silence per the rule.
(b) Unsure it cleared the bar: the $5,000 dividend. The announcement itself was Wed. Sept. 9, so it
  predates Friday's brief — which covered the convention's closing but missed the dividend
  entirely. I ran it framed on the Sept. 10–13 development (bipartisan pushback, Vance narrowing it
  to exclude the wealthy, the legal question about conditioning payments on an election result)
  rather than on the announcement. Defensible, but it is a gap-fill for a miss, not fresh news.
  Also borderline: the IAA Transportation bullet is a preview of a press day happening today, so it
  is forward-looking rather than reported — I cited electrive's Sept. 13 preview and Automotive
  World's Renault piece rather than claiming the Kia PV7 reveal I could not yet confirm had run.
(c) Process: the three standing audits (stale-date grep, class-name grep, domain-vs-display-name)
  all ran clean — 34/34 links matched their displayed source names, no leftover "September 11"
  strings. The domain audit has now caught something on two of four runs, so keeping it is right.
  Egress this run: news.usni.org and www.nfl.com both EGRESS_BLOCKED, and the search API rejects
  arstechnica.com and wired.com in allowed_domains (add these to the known-rejected list alongside
  reuters/guardian/nytimes/wsj/politico/theverge). thepourover.org stayed blocked, so the
  water-cooler gate again ran on wire/public-broadcaster consensus alone — that is now three
  consecutive runs and the routine's TPO step should be rewritten or dropped rather than retried.
(d) Tweak next run: I spent two searches chasing NBA content (Blazers/Warriors) that does not exist
  — camp opens Sept. 29 and the Sept. 9 brief already said the offseason is quiet. Until media day,
  skip the NBA pass entirely and go straight to Padres + one non-NBA item; CLAUDE.md's "NBA first"
  ordering is a preference, not a requirement to search for nothing. Second: last run's note about
  dropping stories that only surface on aggregators paid off — the OpenAI/Google/Meta search
  returned nothing but LLM-tracker farms and I dropped it on the first pass as intended.
Date-excluded this run: Padres ownership introduction (Aug. 24, 21 days — KPBS's homepage summary
made it look current); Warriors Hawaii camp (Aug. 31, and forward-looking to Sept. 29); Kia PV5
ten-body-style expansion (Sept. 9, carried Sept. 11); Sony DP7/DP5 control monitor and Atomos
Shinobi 7 II (both carried Sept. 11). Mito exclusions were relevance, not date: the ND6 allotopic
paper (covered Sept. 9), the CEUS perfusion study and TK2 masterclass (excluded again — fifth
consecutive for TK2), the endothelial-coupling review, riboflavin/complex-I case reports, the MASLD
MitoQ-vs-SS-31 mouse study, the ASCENT oocyte review and two general mitochondria reviews.
Mito item that ran: PNAS scMPCDS (Aug. 31, 14 days exactly — at the edge of the window). It
qualified on the DdCBE off-target finding, which is a real safety signal for the heteroplasmy-
reduction route, not on the platform paper's novelty alone. Cited pnas.org, PubMed and doi.org
separately so each displayed name matches its own domain — the fix for last run's doi.org error.
Quote: Swinton is still oldest in rotation but remains unverifiable per QUOTES.md, so fell through
to Chambers (12 days), different passage from the Sept. 2 "built for the valley" line.

## 2026-09-16 (Wed)
(a) Thin/empty: 🧬 Mito omitted entirely — correct call, see below. School ran 1 bullet (only one new
  qualifying email since Monday; the 9/13 director letter was already mined by the Sept. 14 issue).
  Kauai 1, Tech 2, World 2, US 2 — a genuinely quiet 48 hours, not under-searching.
(b) Unsure of the bar: the Kauai bullet. 76%→82% is incremental and on its own would not run; it
  cleared because schools reopening and the Princeville–Wainiha isolation are new facts, not a
  restatement of the percentage. If next Friday is only another percentage, drop it.
  Also the Tilta FX5 bullet — the reader shoots an FX6, not an FX5, so it ran on the rigging
  hardware (ARCA plate, DJI centring point) being body-agnostic rather than on the camera.
(c) Mito: omitted. Everything in the 14-day window failed the filter, not the date — two case
  reports (MELAS peritoneal dialysis, MT-ND4 anaesthesia encephalopathy), an RIRCD case series, a
  vitamin/cofactor prescribing survey, and four reviews (oxygen delivery, CLPP, endothelial
  coupling, TK2 masterclass — the last two now excluded for the sixth consecutive run). The ND6
  allotopic JCI Insight paper resurfaced in the search and was correctly caught as already covered
  Sept. 9. The taurine/zagociguat/PRIZM material that the IRDR review surfaces ran Aug. 27, so the
  review-article exception does not reopen it.
(d) GW watch: no bullet. USNI's Sept. 14 fleet tracker still has CVN-73 in the Arabian Sea with
  CVW-5 and USS Shoup — position unchanged, no incident, so silence was the correct output.
(e) Tweak next run: the two Tech bullets (labs coordinating on safety, OpenAI IPO delay) are really
  one story about the same safety-pressure moment; next time collapse a pair like that into one
  synthesised bullet and spend the slot on consumer/practical tech, which has now been absent two
  runs running. Apple correctly yielded nothing — iOS 27 shipped into the Sept. 14 issue and there
  was no Sept. 15–16 follow-on.
Egress this run: espn.com, cined.com and newsshooter.com all EGRESS_BLOCKED on direct fetch (add to
  the known-blocked list with usni.org and nfl.com); search-only worked fine for all three. The
  Padres score needed two passes because one search result conflated a Sept. 15 Rockies loss with an
  8–7 Padres win from a different date — verified against the ESPN recap gameId before writing.
Drive: the rotation path worked end to end this run (reparent + rename), so the fallback was not
  needed. Note for a future cleanup: eight stale "Latest.html" files from May still sit in the
  folder root from the pre-"Current Brief" scheme. Left alone — out of scope for a per-run rotation.
Quote: Swinton still unverifiable and skipped per QUOTES.md, so next-oldest was Augustine (09-04);
  used Sermon 169 rather than another Confessions passage to avoid a third Confessions in five weeks.

## 2026-09-18 (Friday)
(a) Thin/empty: Gear 1 (IBC ran Sept 11-14 and the last two issues already mined it — Sirui Saturn V2
  was the one genuinely uncovered item left, so one bullet is honest rather than thin). EV 1 — no new
  van/family story at all since the Sept 16 Kia PV7 and Renault Trafic bullets, so the one allowed
  general item (NHTSA/Cybercab) carried the section. School 1: only three emails since Monday and all
  three were the same lockdown thread. Sports 2, both non-NBA — camps do not open until Sept 29 and
  there was no Blazers/Warriors news in the window; the Sharpe meniscus surgery surfaced in search but
  dates to Aug 26-27 and was out of the lookback.
(b) Unsure of the bar: the Houthi/Bab el-Mandeb bullet. The underlying captures are Sept 11-14, i.e.
  before the last brief, and the Sept 16 issue simply did not run them. I ran it on the "what is new
  since we last covered this" test against the Sept 11 Mokha bullet — Perim, the Hanish islands and the
  completed coastline takeover are all new facts — rather than on same-day freshness. If a similar gap
  shows up again, that is the right test, but flag it. Also the Kauai bullet: the self-review from last
  run said drop it if it is only another percentage, so I led on the Wainiha/Hā'ena helicopter repair and
  the end-of-next-week ETA and used 91% only as context. That held the line.
(c) Mito: omitted, sixth consecutive run. Everything in the window failed relevance, not date — forensic
  mtDNA papers (EDNAP heteroplasmy concordance, telogen hair panels, thermal degradation in teeth), a
  string of TCM/nanozyme mitochondria-adjacent bench papers, an iPSC neuronal deletion model, and the
  MELAS peritoneal-dialysis case report already caught and excluded last run. The CHOP zebrafish
  "drug in MELAS trials works in other mito models" story surfaced and looked promising until the date
  check: the release is August 2025. Correctly excluded.
(d) GW watch: no bullet, second consecutive quiet run. The Sept 14 USNI fleet tracker is still the most
  recent position report — CVN-73 with CVW-5 and USS Shoup in the Arabian Sea, unchanged, no incident,
  no claim. CENTCOM's Sept 16 "Hormuz remains open" line is theatre-wide, not ship-specific, so it went
  into the World Houthi bullet as context and not into a GW item. Silence remains correct.
(e) Tweak next run: last run's note said to collapse paired same-moment AI stories and spend the slot on
  consumer/practical tech. Did that — the OpenAI misalignment disclosure is one bullet, not two, and the
  iOS 27.2-before-27.1 item is the first practical Apple bullet in three runs. Keep that. Next tweak:
  the EV section has now been van-less for one run and will likely stay so until the next commercial-
  vehicle show, so consider letting a family-format EV *policy* story (charging, tax credit, pricing)
  count as priority rather than filler when no new van model exists.
Egress this run: timesofsandiego.com, chop.edu and mlb.com all EGRESS_BLOCKED on direct fetch — add to
  the known-blocked list alongside espn.com, cined.com, newsshooter.com, usni.org, nfl.com. Search-only
  worked for all three. The Padres record needed care: the Sept 14 and Sept 16 issues disagree with each
  other (80-68 vs 82-68), so I cited the AP recap's own framing — four games clear of Arizona with nine
  to play — instead of carrying forward a W-L number I could not reconcile.
Conditions: the scheduled 11:20/11:45 UTC fetches did not land — data/conditions.json was still the
  Sept 16 17:17Z file at run time. Manual actions_run_trigger worked and returned fresh data in ~10 min.
  Worth watching: if the scheduled runs miss again on Monday, the workflow cron needs a look.
Tide gap: the fetched prediction set contained only three entries starting at the 2:35 PM high, so
  today's morning low is genuinely absent rather than omitted. Flagged in the data-note per the
  data-integrity rule instead of interpolating.
Quote: Swinton still skipped per QUOTES.md. Next-oldest was MLK (09-07), and both prior MLK entries
  (Birmingham Jail 08-23, "Suffering and Faith" 09-07) were inside 30 days, so I went to a third source
  — "Shattered Dreams" from Strength to Love — and verified the wording against the King Institute at
  Stanford rather than a quote-aggregator.

## 2026-09-21 (Mon)
(a) Thin/empty: Mito omitted entirely — see below. Kauai ran 1 (correct, the story is now a
  two-town tail). No NBA item: camps do not open until Sept 29 and the only Blazers news in
  range (coaching staff, Sept 10) predates the Friday lookback, so Sports led with MLB. EV ran 2,
  the second marked "(general EV news)" per the cap rule.
(b) Unsure it cleared the bar: the San Diego gas-price bullet. It ran Sept 18 at "29th in 30 days,
  $6.157" and this is "31st in 32 days, $6.19." I framed it on the new four-month high rather than
  the counter, but it is the weakest item in the issue and a third real SD story would have pushed
  it out. Search for SD local on a Sunday/Monday is consistently the thinnest part of the run.
(c) Mito: the one genuinely strong candidate was the Stanford myeloid-cell-replacement /
  intercellular mitochondrial-transfer paper in Nature Communications (PMID 42736305) — it entered
  PubMed this window but was PUBLISHED Aug 15, so the "use the older date" rule excludes it at 37
  days. Everything else in the window was case reports (MELAS peritoneal dialysis, RIRCD), a
  Finsterer letter, an oxygen-delivery review restating the known hypoxia work, and a PDE5
  editorial (Mol Genet Metab, Sept 16) with no abstract and no findable companion study — I could
  not verify what was new, so it did not run. Section omitted, header and all.
(d) Tweak next run: the Nature Communications miss is worth a rule check with the reader. A
  landmark mito paper indexed 5 weeks after online publication will ALWAYS fail the 14-day gate,
  which means the strict filter and the date filter can combine to make the section structurally
  unable to report the biggest results. Consider proposing a narrow carve-out: for Mito only,
  allow up to ~45 days from publication date, since the anti-repetition rule already prevents
  re-running anything covered. Do not change it unilaterally — raise it in the chat reply.
Conditions: DIAGNOSED. The cron in fetch-conditions.yml is correct (20/45 past 11 and 12 UTC,
  Mon/Wed/Fri). The problem is GitHub's scheduler delivering the runs hours late: on Sept 18 the
  four scheduled runs actually fired at 15:11, 16:24 and 16:44 UTC — 3.5 to 5 hours behind their
  cron times, i.e. long AFTER the brief published. Same today, which is why the file was still the
  Sept 18 16:44Z copy. GitHub documents cron as best-effort and delays are worst at heavily used
  minutes; :20 and :45 on the hour boundary are exactly that. This is NOT the DST or day-of-week
  logic and it is not a repo bug — do not "fix" the cron days. The fix worth proposing to the
  reader is moving the schedule an hour or two earlier and onto odd minutes (e.g. 07/37 past
  09 and 10 UTC) to buy slack, and keeping the manual actions_run_trigger as the reliable path.
  Manual trigger again returned fresh data in ~8 minutes.
Surf: reported OUTLOOK as unavailable rather than guessing. conditions.json carries live buoy
  readings only, no forecast model, and a single time-slice cannot tell building from fading —
  Friday's reading was a different swell (3.0 ft @ 14s from 183) so it is not a usable baseline.
GW watch: nothing verifiable since the last brief. Latest USNI material (Sept 13-14 fleet tracker,
  a routine Super Hornet recovery) predates the Friday issue and restates a known position.
  No bullet — silence is the correct output.
