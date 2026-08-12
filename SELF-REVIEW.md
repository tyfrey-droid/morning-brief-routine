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
