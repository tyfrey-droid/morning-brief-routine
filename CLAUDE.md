# Morning Brief — repo notes for the daily routine

## Weather & Surf data: use data/conditions.json (NOT direct fetch)

This sandbox's egress policy blocks api.weather.gov, ndbc.noaa.gov,
tidesandcurrents.noaa.gov, stormsurf.com, and WebFetch generally (all
return 403). Do NOT burn time re-testing them.

Instead, a GitHub Actions workflow (`.github/workflows/fetch-conditions.yml`)
runs on GitHub's runners (which have normal internet access) and commits
live data to `data/conditions.json`:

- NWS point forecast for La Mesa 91942 (today/tonight/tomorrow periods)
- NDBC buoy 46258 (Mission Bay West) & 46225 (Torrey Pines): wave height (ft),
  dominant period (s), mean direction (deg), water temp (°F)
- NOAA tide predictions for San Diego station 9410170 (today + tomorrow,
  Pacific time, hi/lo)

It runs at 11:20, 11:45, 12:20 & 12:45 UTC on the brief's publish days
(Mon/Wed/Fri). Two of those four land at 4:20 & 4:45 AM PT — just before the
brief's 4–6 AM PT slot — in whichever DST regime is current; the other pair
fires harmlessly and just refreshes. On any run day, if the data is stale,
trigger a fresh fetch on demand (step 2 below). Each run:

1. `git pull origin main`, read `data/conditions.json`, check `fetched_at_utc`.
2. If it is older than ~2 hours, trigger a fresh run via the GitHub MCP tool
   `actions_run_trigger` (workflow file: `fetch-conditions.yml`, ref `main`),
   wait ~60–90 s, then `git pull` again.
3. Build the 🌤 Weather and 🌊 Surf sections from the JSON. Cite it as live
   NWS/NOAA data with the observation/fetch time.
4. If a field is null (buoy offline, fetch failed), show "unavailable" for
   that row — one-sentence note max. Never invent a reading.

Buoy notes: 46258/46225 are Scripps Waverider buoys — wave + water temp only,
no wind. For wind, use the NWS forecast periods' windSpeed/windDirection.

## Other standing notes

- GitHub Pages deploys from `main`. Always commit index.html +
  archive/YYYY-MM-DD.html to `main` — never a feature branch.
- Before writing content, `git pull origin main` FIRST and read the last
  ~7 days of archive/ briefs for the anti-redundancy filter (a previous run
  drafted against a stale clone and had to redo several sections).
- Every bullet: bolded 3–8 word headline (`<strong>`) then 1–3 sentence
  summary, links whose display name matches the linked domain.
- Section order: World · US & Politics · Tech & AI · 🏀 Sports (NBA: Blazers
  first, Warriors second, league-wide; max 1–2 big non-NBA items) ·
  San Diego · 🌺 Kauai (max 2) · Filmmaking Gear · Electric Vehicles (max 3) ·
  🧬 Mito Research (omit entirely — no header — when nothing meets the strict
  bar) · Weather · Surf · closing quote.
- REMOVED sections — do NOT include (dropped 2026-08-06 by reader request):
  ✨ One Good Thing and 📅 On This Day. The closing theologian quote stays.

## Release cadence: Monday / Wednesday / Friday only

Changed 2026-08-06 by reader request. The brief is a Mon/Wed/Fri publication,
not a daily one — a Pour-Over-style longer cadence so each issue carries
stories with staying power rather than 24-hour-cycle churn.

1. GATE FIRST — unless a human asked for this run (see "Manual override"
   below). At the very start of every run, check the current Pacific-time day
   of week. On Monday, Wednesday or Friday, publish normally. On any other day,
   do NOT gather, write, commit, or push anything — log "Off-cadence day
   (<weekday>) — no brief today" and stop immediately. Keep the off-day path
   cheap — no searches, no connectors.
2. LOOKBACK = since the previous brief. Determine the date of the most recent
   archive/ file and gather news published since then (typically ~48–72h:
   Fri→Mon spans the weekend). Prefer developments that still matter now over
   things that merely happened; when a story ran in the last brief, lead only
   with what is genuinely new since.
3. Weather/Surf are still point-in-time for publish day — use the freshest
   data/conditions.json as before. On an off-day manual run the scheduled
   fetch will not have fired, so expect stale data: trigger
   `fetch-conditions.yml` via `actions_run_trigger` (it keeps
   `workflow_dispatch` for exactly this), wait ~60–90 s, then `git pull`.

### Manual override — an off-day run a human asked for DOES publish

The gate exists to stop an *unattended* scheduler, never to refuse the reader.
Publish on an off-day — running the full normal pipeline — in either case:

- **Explicit in-session request.** A human asks for the brief in conversation
  ("run it now", "publish today"). Always honor this; do not ask twice.
- **"Run now" from the routines pane.** This arrives as the stored prompt and
  can look identical to an automated firing, so use the clock to tell them
  apart. The scheduled slot is the 4–6 AM PT window (target ~5:00 AM PT). An
  off-day firing OUTSIDE roughly 3:30–7:00 AM PT is a human pressing the button
  → publish. An off-day firing INSIDE that window is likely a stray automated
  run → apply the gate and stop.
  (The external trigger is itself set to Mon/Wed/Fri, so off-day firings should
  be rare and are almost always manual; the window check is only
  defense-in-depth in case a daily schedule ever returns.)

When publishing off-cadence: note it in the final report, use the normal
"since the previous brief" lookback, and write index.html + the dated archive
as usual. That issue then counts as "the previous brief" for the next run.

### UTC-skew guard — a "gated" firing may BE the publish-day run (outage fix)

Observed Aug 7–11, 2026: the external trigger was configured on UTC weekdays
(Mon/Wed/Fri at ~04:10 UTC ≈ 6 AM UTC+2), so every firing arrived ~9 PM PT on
Sunday/Tuesday/Thursday — an off-cadence Pacific day. The gate stopped each
one and NO brief published for nearly a week, while `fetch-conditions.yml`
(correctly on UTC cron) kept refreshing data for briefs that never came. The
gate must never cause a silent total outage again:

1. If an unattended firing lands on an off-cadence Pacific day but its **UTC
   weekday is a publish day** (equivalently: it is the evening before a
   publish day, roughly 4 PM PT–midnight), it is the publish-day trigger
   arriving early, not a stray. Do NOT gate — run the full normal pipeline
   and publish. Date the issue with the actual Pacific date and note the
   early/off-slot publish in the report.
2. Dedupe guard: if the newest archive/ file is from today or a brief was
   published within ~12 hours, log "issue already published — skipping
   duplicate firing" and stop.
3. The real fix is the trigger's schedule. The reader confirmed on 2026-09-01
   that they want the brief written in the early-morning hours, **4–6 AM PT**,
   not the night before. Target ~5:00 AM **America/Los_Angeles** Mon/Wed/Fri
   (= 12:00 UTC during PDT, 13:00 UTC during PST). Only the account owner can
   change it in the routines pane. Until firings start arriving in the
   4:00–6:00 AM PT window, keep flagging the misconfiguration in every final
   report.
4. Once firings do arrive in that window, the UTC-skew path in 1. should stop
   triggering. Do not delete it — it is the outage backstop if the schedule is
   ever reset to UTC weekdays — but a run that publishes via 1. after the fix
   is a signal the trigger reverted, and the report should say so plainly.

## Story counts: small by default, with headroom

- The goal is still a tight, high-signal brief — a handful of items, not a
  firehose. Do not pad to fill space; an empty or 1-item section is fine.
- But the longer cadence means real news accumulates. When genuinely
  qualifying stories exist, allow headroom: World / US up to 5 (was 4),
  Tech, Sports, San Diego, Gear up to ~8 each, EV up to 3, Kauai up to 2.
  These are ceilings for busy stretches, not targets. Quality bar is
  unchanged — every added item must independently clear it.

## Reader feedback loop (self-improvement)

The published brief carries a per-story feedback control (see the flag button
in index.html). Clicking it opens a pre-filled GitHub issue labeled
`brief-feedback` against tyfrey-droid/morning-brief-routine.

At the START of each run (after the cadence gate, before selecting stories):
- Read open issues via the GitHub MCP tools (search issues with label
  `brief-feedback`, state open). Honor them:
  - "already read" / "redundant" → exclude that story AND its underlying
    development from this brief; treat like the anti-redundancy filter.
  - "not relevant" → down-weight that topic/source going forward.
  - "more like this" → up-weight that topic/source when it recurs.
- After acting on a feedback issue, close it via the GitHub MCP tools with a
  one-line comment noting how it was applied (so it isn't re-processed). Keep
  comments minimal.

## Self-evaluation (bounded — must not burn usage)

Keep this cheap: no extra web searches, no subagents, no separate model calls.
At the END of each successful publish, append a 3–5 line entry to
`SELF-REVIEW.md` on main (create if missing) covering only: (a) which sections
were thin/empty and why, (b) any story you were unsure cleared the bar,
(c) one concrete tweak to try next run. Read the last ~3 entries at the start
of a run to avoid repeating mistakes. This file is internal notes, never
published to Pages. If time/tokens are short, skip it — it is best-effort.
