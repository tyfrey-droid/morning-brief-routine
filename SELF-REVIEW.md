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
