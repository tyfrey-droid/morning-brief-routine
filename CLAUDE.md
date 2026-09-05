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
  bar) · 🎒 School (same omit-entirely rule) · Weather · Surf · closing quote.
- REMOVED sections — do NOT include (dropped 2026-08-06 by reader request):
  ✨ One Good Thing and 📅 On This Day. The closing theologian quote stays.

## 🎒 School — added 2026-09-05 by reader request

A short section pulled from the school's email, so the week's classroom
topics, dates and parent action items land in one place instead of across a
dozen newsletters.

### Gmail is now READ-ONLY allowed, for this section only

This supersedes the "never touch Gmail" / "Gmail is never used" lines in the
stored routine prompt, changed 2026-09-05 by explicit reader request. The
carve-out is narrow and absolute at its edges:

- ALLOWED: `search_threads` and `get_thread` against school senders, to build
  this section.
- NEVER: send, reply, forward, draft, label, archive, trash, or mark spam.
  Never read mail outside the school scope below. Never quote a private
  one-to-one message from a teacher — this section is for mail sent to all
  families, not correspondence about a specific child.
- If a Gmail call fails or the connector is unavailable, log it and omit the
  section. Never guess at school content from memory.

### Scope: whose mail, and how far back

Micah (4th grade) at High Tech Elementary Mesa. Search since the previous
brief's date — the same lookback every other section uses:

    from:hightechhigh.org OR from:schoolsoft.com OR from:schoolmintemails.com
    after:YYYY/MM/DD

Recurring senders worth knowing: the 4th-grade classroom newsletter, the
performing-arts teacher, the school director, and the School Family
Association (SFA) blasts. `noreply@` addresses carry the school-wide
announcements; the classroom newsletter carries the actual curriculum.

### What qualifies

INCLUDE: what the class is actually studying this week; dates and deadlines;
anything needing a parent to DO something (forms, signatures, volunteer
slots, supplies, permission slips); school-wide policy that changes something
(meal programs, drop-off rules, calendar changes).

EXCLUDE: fundraising and donation appeals with no action attached; spirit-wear
marketing; menu emails unless the policy changed; the third restatement of an
event already covered; anything already carried in a prior brief unless the
details moved. Standard anti-redundancy applies — a date announced three
briefs ago is not news again until it is imminent or changed.

Surface genuinely time-sensitive items FIRST — a form due before the next
brief, a volunteer day this weekend, a mandatory performance.

### Emi's IEP / SDUSD advocacy thread — EXCLUDED by default

Do NOT put the special-education dispute, IEP correspondence, CDE complaint,
attorney or advocate mail into this section or any other. It is sensitive,
it is legally live, the reader is already a participant, and (see below) this
brief is public. Only include it if the reader asks in-session, and even then
only in the chat reply, never in the published HTML.

### PRIVACY — this repo and its Pages site are PUBLIC

Verified 2026-09-05: `tyfrey-droid/morning-brief-routine` is a public repo
with public GitHub Pages, and every archive/ issue is permanently readable by
anyone. So the published section is written DE-IDENTIFIED by default:

- Say "4th grade," never the child's name, and never a room number.
- Refer to "the classroom teachers," "the performing-arts teacher," "the
  school director" — no staff names, no staff email addresses.
- Do NOT name the school or district in the published HTML.
- No links into Google Docs/Photos/wishlists from the school mail — those
  URLs are effectively unlisted credentials for a private community.
- No drop-off/pick-up procedures, room assignments, or anything describing
  where a specific child physically is at a specific time.

Curriculum topics, dates, and "a form is due Tuesday" all survive this
intact, which is the actual value. The reader knows who his kid's teacher is.
If he ever asks for full detail with names, that is his call to make — but it
should be a deliberate choice, and the right fix first is making the site
private, not quietly loosening this rule.

### Length

Same discipline as everywhere else: a handful of bullets, ~4 max. Group into
"this week in class," "coming up," and "needs you" only if there is enough to
warrant it — otherwise a flat list. **Omit the section entirely, header and
all, when nothing qualifies** (the 🧬 Mito rule). An empty week is normal:
holidays, breaks, and Wednesday issues will often have nothing new since
Monday. Never pad it to justify its existence.

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
  apart. As of 2026-09-01 the trigger fires at **5:30 AM PT on weekdays**
  (Mon–Fri), so the scheduler's Tue/Thu arrivals are tightly clustered around
  5:30. An off-day firing INSIDE roughly **5:15–5:50 AM PT** is that scheduler
  → apply the gate and stop. An off-day firing at any other hour is a human
  pressing the button → publish.
  Keep this window tight. It used to be 3:30–7:00 AM, which was safe when
  off-day firings were rare, but Tue/Thu firings are now routine and a wide
  window would swallow a genuine 6 AM "Run now" on one of those days —
  refusing the reader, which the gate must never do.
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
3. **RESOLVED 2026-09-01.** The reader reset the trigger to **5:30 AM PT,
   weekdays (Mon–Fri)** — inside the 4–6 AM PT window they asked for. Firings
   now land on the correct Pacific day, so **stop flagging the schedule as
   misconfigured in the final report.** Nothing further is owed on this.
4. The UTC-skew path in 1. should no longer trigger: a 5:30 AM PT firing has
   the same UTC calendar day (12:30 UTC in PDT, 13:30 in PST), so the
   "evening before" condition cannot match. Do NOT delete it — it is the
   outage backstop if the schedule is ever reset to UTC weekdays — but if a
   run ever publishes via 1. again, that means the trigger reverted, and the
   report should say so plainly.
5. The trigger fires **five** days a week against a **three**-day cadence.
   That is expected and correct, not a bug: Tue/Thu firings hit the gate in
   "Release cadence" step 1 and stop cheaply without searches or connectors.
   Do not report a gated Tue/Thu firing as an error or a schedule problem —
   log the one-line off-cadence message and stop. `fetch-conditions.yml`
   stays on Mon/Wed/Fri only; there is no reason to fetch conditions for a
   brief that will not be written.

## Story counts: small by default, with headroom

- The goal is still a tight, high-signal brief — a handful of items, not a
  firehose. Do not pad to fill space; an empty or 1-item section is fine.
- But the longer cadence means real news accumulates. When genuinely
  qualifying stories exist, allow headroom: World / US up to 5 (was 4),
  Tech, Sports, San Diego, Gear up to ~8 each, EV up to 3, Kauai up to 2,
  School up to 4. These are ceilings for busy stretches, not targets. Quality
  bar is unchanged — every added item must independently clear it.

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
