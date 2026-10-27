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
- Swell forecast (`swell_forecast_open_meteo`, added 2026-10-27): Open-Meteo's
  marine model just off Mission Beach, 4 days of daily max wave height,
  swell height (ft), swell period (s) and dominant swell direction (deg)

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

Surf OUTLOOK row: build it from `swell_forecast_open_meteo` — compare today
against the next 2–3 days ("SSW swell holding ~3 ft at 13s through Wednesday,
dropping to 2 ft Thursday") and cite it as the Open-Meteo marine model in the
source note. It is a model forecast; the buoys stay the source for current
readings. stormsurf.com is blocked from this sandbox (connect_rejected by the
egress policy, confirmed 2026-10-27); if the reader allowlists it and a fetch
succeeds, prefer stormsurf's QuikCAST wording for the outlook and use the
model as the cross-check. If the forecast field is null, fall back to the
buoy-to-buoy trend between consecutive conditions.json commits.

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
  San Diego · 🌺 Kauai (max 2) · Filmmaking Gear · 🔋 F-150 Lightning & EVs
  (max 3, +1 gadget pick — see the 🔋 section below) ·
  🧬 Mito Research (omit entirely — no header — when nothing meets the strict
  bar) · 🎒 School (same omit-entirely rule) · Weather · Surf · closing quote.
- REMOVED sections — do NOT include (dropped 2026-08-06 by reader request):
  ✨ One Good Thing and 📅 On This Day. The closing theologian quote stays.
- STANDING WATCH: USS George Washington (CVN-73) — see the ⚓ section below.
  Flag any news involving that ship inside World or US & Politics. Exempt from
  the consensus rule and from the section bullet cap; strict sourcing and a
  privacy rule apply.

## 🔋 F-150 Lightning & EVs — refocused 2026-10-27 by reader request

The reader bought a **2023 Ford F-150 Lightning** and the EV section now
centres on that truck. This SUPERSEDES the stored routine prompt's
"Electric Vehicles" rules (van/family-EV priority, "(general EV news)"
filler marker) and the old "CHANGE 3" EV cap language.

Section label: `🔋 F-150 Lightning & EVs`. Max 3 bullets. Priority order:

1. **F-150 Lightning items first** — anything that matters to an owner of a
   first-generation (2022–2024 model year) Lightning:
   - recalls, service campaigns and TSBs (check NHTSA's recall database and
     Ford's own notices for the 2023 Lightning by name);
   - Ford Power-Up over-the-air software releases and what they change;
   - charging: Tesla Supercharger / NACS adapter access and pricing, Ford
     charging network changes, home charging and Intelligent Backup Power /
     Ford Charge Station Pro updates, BlueCruise subscription changes;
   - battery, warranty, range or towing findings with real data;
   - the Lightning program itself (production status, successor, parts and
     service support for a discontinued model), and used-market value;
   - **accessories and mods**: new bed, frunk, tonneau, rack, lighting,
     charging and power accessories made for the Lightning; popular owner
     mods and fixes. Practical, specific, with price when known.
   - **Fun gadgets and accessories** (reader request, 2026-10-27): the
     enjoyable side of owning the truck, not just fixes. Things that use
     what the Lightning is good at: Pro Power Onboard and the frunk (camp
     cooking, coffee makers, induction cooktops, portable fridges, lighting,
     projectors, power tools), tailgate and bed gear, camping and overland
     kit, clever organisers, cabin tech, kid- and dog-friendly add-ons.
     Aim to include ONE such pick in most issues when a genuinely good one
     surfaces: something newly launched, newly reviewed, or getting real
     owner buzz in the window. One or two sentences on what it is, why it
     suits the Lightning, and the price. It may run as a 4th bullet on top
     of the 3-bullet cap. Never repeat a gadget carried in the last 30 days.
     Sources: maker announcements, bylined reviews (The Drive, Car and
     Driver, MotorTrend, Electrek, Gear Patrol, Wirecutter), and owner
     threads on the forums below ("what did you add to your Lightning").
     Not affiliate listicles ("15 best F-150 accessories") — find the
     product there if you like, but cite the maker or a real review.
2. **At most ONE EV van item**, and only if it is a real development
   (a launch, US pricing, a confirmed US arrival). Vans are now secondary.
3. **General EV news only when it is big** — federal policy or tax credits,
   a charging-network shake-up, a major automaker strategy change, a
   landmark launch. When the week's biggest EV story is general, it may
   take the whole section; do not pad with minor general items.

Lightning news is sparse (older, discontinued model). An empty or 1-bullet
section is fine; omit the section entirely, header and all, when nothing
qualifies. Lightning items may run up to the 14-day date limit even when
older than the previous brief, as long as they were not already carried.

### Sources

- Primary: Ford (media.ford.com, ford.com owner/support pages), NHTSA
  (nhtsa.gov recalls), Ford Pro.
- News: Electrek, InsideEVs, Ford Authority (fordauthority.com), The Drive,
  Car and Driver, MotorTrend, Green Car Reports, CleanTechnica.
- **Owner communities — reader-approved carve-out from the reputability
  bar:** F150LightningForum.com, the Lightning boards on F150gen14.com, and
  Reddit's r/F150Lightning. Comb them for mods, accessories, software
  release notes and issues many owners are reporting. Rules:
  - Prefer them as a discovery signal: when a forum thread points to a
    Ford notice, NHTSA filing or news article, cite that instead.
  - Cite the forum directly only when the item IS community knowledge (a
    popular mod, a widely reported quirk, an owner-measured result). Label
    it in the text as owner reports, never as fact ("Owners on the
    Lightning forum report…"), and require several independent owners or
    an active thread, not one post.
  - Display names must match the domain: "F150 Lightning Forum" →
    f150lightningforum.com, "F150gen14" → f150gen14.com, "r/F150Lightning"
    → reddit.com.
  - No affiliate-link product roundups, no dealer marketing, no YouTube
    hype channels as sources.

### Privacy

Same public-repo rule as everywhere else: write it as ordinary EV coverage.
Do not say "your truck" or "our truck", or otherwise publish that the reader
owns one; no VIN, dealer, purchase or location details.

## ⚓ USS George Washington watch — added 2026-09-13 by reader request

The reader knows someone serving aboard **USS George Washington (CVN-73)**,
currently deployed to the CENTCOM AOR in the Arabian Sea near the Strait of
Hormuz, in the middle of the US–Iran conflict. Standing instruction: **flag any
news involving that ship.**

### How to run it

- This is a WATCH, not a new section. The item goes in 🌍 World or 🇺🇸 US &
  Politics — whichever fits — as a normal bullet, with the ship named in the
  bolded lead-in so it is unmissable on a skim (e.g. "**George Washington rides
  out a missile claim**"). Do not create a standing header; an empty week gets
  no bullet at all.
- It is EXEMPT from the World/US consensus rule (leading on 2+ outlets). A
  single credible defense outlet is enough here — USNI News, The War Zone
  (twz.com), Task & Purpose, Stars and Stripes, Defense News, Military.com, or
  a CENTCOM/Navy release. The consensus test exists to pick water-cooler
  stories; this one is personal and does not need to clear it.
- It does NOT count against the section's bullet cap. If World already has its
  four, the GW item is a fifth.
- Anti-redundancy still applies in the normal way: run it when there is a
  genuine development (position or homeport change, strike or damage claim,
  named casualties, relief by another strike group, deployment extension,
  incident aboard), not for a restatement of where she already was.

### Accuracy discipline — the point is to be trustworthy, not fast

This is the one item in the brief where the reader has someone's safety at
stake, so the bar on sourcing is HIGHER than elsewhere, not lower:

- ALWAYS separate claim from confirmation. Iranian state media and IRGC
  statements routinely claim strikes on US vessels that CENTCOM then denies;
  as of 2026-09-13 no hit on CVN-73 has been independently confirmed. Write
  "Iran's IRGC claimed X; CENTCOM denied it" — never launder a claim into a
  fact, and never lead with the claim's framing.
- Content farms and SEO aggregators pick up these claims hard and strip the
  denial. If a strike claim appears ONLY on such sites, it does not run. Check
  a real defense desk before writing anything alarming.
- Never speculate about the safety of any individual crew member, and never
  estimate casualties ahead of official confirmation.
- Tone: the brief's standing "informed, not alarmed" rule applies with extra
  force. Report position, orders and confirmed events plainly. No dramatics.
- If nothing verifiable happened, say nothing. Silence is the correct output
  for a quiet week, and a reader with someone aboard will read an invented
  item as much worse than no item.

### PRIVACY — do not publish the personal connection

The repo and its Pages site are public (see the School section's privacy note,
which applies here for the same reasons, with an added force-protection edge).

- NEVER state or imply in the published HTML that the reader knows someone
  aboard, has family or a friend on the ship, or has any personal stake in it.
  The bullet reads as ordinary news coverage and nothing more.
- Never name the service member, their rate/rank, division, job, or any detail
  that could identify them, in the HTML or in a commit message.
- Do not publish anything about the ship's future movements, port calls,
  schedule, or return date beyond what the Navy or a major outlet has already
  announced publicly. Do not aggregate ship-tracker or AIS data.
- The reader can of course ask for more detail in-session; answer freely in the
  chat reply. The restriction is on what gets committed and published.

## 🎒 School — added 2026-09-05, two schools since 2026-10-26 (reader request)

A short, skimmable section pulled from school email, so the week's dates,
reminders and parent action items land in one place. It now covers BOTH
children's schools (Emi's added 2026-10-26).

### Gmail is now READ-ONLY allowed, for this section only

This supersedes the "never touch Gmail" / "Gmail is never used" lines in the
stored routine prompt, changed 2026-09-05 by explicit reader request. The
carve-out is narrow and absolute at its edges:

- ALLOWED: `search_threads` and `get_thread` against the school senders
  below, to build this section.
- NEVER: send, reply, forward, draft, label, archive, trash, or mark spam.
  Never read mail outside the school scope below. Never quote a private
  one-to-one message from a teacher or administrator — this section is for
  mail sent to all families, not correspondence about a specific child.
- If a Gmail call fails or the connector is unavailable, log it and omit the
  section. Never guess at school content from memory.

### Scope: whose mail, and how far back

Lookback for both: since the previous brief's date (`after:YYYY/MM/DD`), the
same lookback every other section uses.

**Micah (4th grade), High Tech Elementary Mesa:**

    from:hightechhigh.org OR from:schoolsoft.com OR from:schoolmintemails.com

Recurring senders: the 4th-grade classroom newsletter (carries the actual
curriculum), the performing-arts teacher, the school director, and the
School Family Association (SFA) blasts. `noreply@` addresses carry the
school-wide announcements.

**Emi, Foster Elementary.** The principal (Gina) sends the school-wide
announcements, and they arrive through PowerSchool's messaging relay, NOT
from her own address. This is an ALLOWLIST: the only Foster mail this
section reads is

    subject:"Emi's administrator" after:YYYY/MM/DD

(subject "Message from Gina Camacho (Emi's administrator)", relayed from a
`…@mail1.attendance.powerschool.com` address). Match the subject, not the
sender — the relay's numeric prefix differs per staff member.

Everything else from Emi's school stays out, unread, because it is about
her specifically rather than the campus:

- The principal's own district email address — almost entirely IEP,
  placement and dispute correspondence.
- "Message from … (Emi's teacher)" relay messages and the teacher's own
  address — day-to-day notes about her care.
- Therapists and specialists (OT, PT, SLP, adapted PE, AAC, eye gaze,
  nursing), district special-programs mail, and the family's advocate.
- Even inside a principal broadcast: anything about Emi specifically, her
  health, feeding, medical care, equipment, therapies, attendance, or
  anything mentioning IEP, assessment, placement or complaint. A real
  broadcast opens to "families" and is about the campus.

When in doubt about an Emi item, leave it out. A missed spirit-day reminder
costs nothing; publishing care or IEP detail costs a lot.

**The weekly Smore is the main Foster newsletter — READ IT.** The
principal's Friday broadcast says "please see the weekly SMORE attached" and
carries a link, `https://app.smore.com/n/3c6ar9`. It is not an attachment: it
is the same URL every week, edited in place, so it always shows the current
issue. Fetch it with WebFetch and pull dates, events, spirit days, minimum
days and parent action items from it, filtered by the same rules as the
email (campus news only, nothing about Emi's care or the IEP). Treat it as
the richest Foster source; the email broadcasts are mostly short reminders.

- If the fetch fails (this sandbox's egress policy refused smore.com as of
  2026-10-26 — the reader is adding it to the environment's allowlist), use
  the broadcast emails alone and say so in the final report: "Foster Smore
  unreachable — section built from email only." One line; do not retry in
  a loop.
- Dojo: the principal also points to ClassDojo. As of 2026-10-26 no Dojo
  mail reaches this inbox, so there is nothing to read. If Dojo emails
  start arriving (from `classdojo.com`), read them under the same filter.
- HTEM: the 4th-grade classroom newsletter's content is in the email body
  itself; read that. Its Google Doc link duplicates it and is not needed.

### What qualifies

INCLUDE: dates and deadlines; anything needing a parent to DO something
(forms, signatures, volunteer slots, supplies, permission slips); schedule
changes such as minimum days, no-school days and spirit/dress-up weeks;
school-wide policy that changes something (meal programs, calendar changes);
and for 4th grade, what the class is actually studying this week (one line).

EXCLUDE: fundraising and donation appeals with no action attached; spirit-wear
marketing; menu emails unless the policy changed; the third restatement of an
event already covered; anything already carried in a prior brief unless the
details moved or it is now imminent (this week or due before the next brief).

Surface time-sensitive items FIRST — a form due before the next brief, an
early dismissal this week, a mandatory performance.

### Emi's IEP / SDUSD advocacy thread — EXCLUDED by default

Do NOT put the special-education dispute, IEP correspondence, CDE complaint,
attorney or advocate mail into this section or any other. It is sensitive,
it is legally live, the reader is already a participant, and (see below) this
brief is public. Only include it if the reader asks in-session, and even then
only in the chat reply, never in the published HTML. The same goes for Emi's
health and care correspondence with school staff.

### PRIVACY — this repo and its Pages site are PUBLIC

Verified 2026-09-05: `tyfrey-droid/morning-brief-routine` is a public repo
with public GitHub Pages, and every archive/ issue is permanently readable by
anyone. So the published section is written DE-IDENTIFIED by default:

- Never a child's name and never a room number. Label which school an item
  belongs to with a short mono tag at the start of the headline:
  **`HTEM`** for Micah's items and **`FOSTER`** for Emi's (reader's choice,
  2026-10-26 — the short school names, used only as tags). Never Emi's
  grade, class type, or anything implying special education.
- Refer to "the classroom teachers," "the performing-arts teacher," "the
  principal," "the school director" — no staff names, no staff email
  addresses.
- Beyond the HTEM / FOSTER tags, do not name the schools, their full
  names, or the district anywhere in the published HTML.
- No links into Google Docs/Photos/wishlists/Smore/Dojo from school mail
  (read the Smore, but never publish its URL) —
  those URLs are effectively unlisted credentials for a private community.
- No drop-off/pick-up procedures, room assignments, exact dismissal times,
  or anything describing where a specific child physically is at a specific
  time. "Friday is a minimum day (early dismissal)" is fine; "dismissal at
  12:05" is not. The reader can get the exact time in chat.

Dates, reminders and "a form is due Tuesday" all survive this intact, which
is the actual value. If the reader ever asks for full detail with names,
that is his call to make — but it should be a deliberate choice, and the
right fix first is making the site private, not quietly loosening this rule.

### Format — SHORT. The reader skims this section.

Requested 2026-10-26: this is a reminders list, not a digest, for BOTH
schools equally — the HTEM classroom newsletter gets the same trim as
Foster (its "this week in class" becomes one short bullet, not a
paragraph). Each bullet is the bolded headline (with the school tag) plus
ONE sentence, two at most.
Only go longer when the item genuinely needs it to be actionable (e.g. a
multi-step form), and even then keep it to the steps.

    <li><strong><span class="tag">HTEM</span> Permission slip due Friday</strong>
    — Sign the fieldwork slip on PowerSchool by Oct 30 or the trip is cancelled.</li>
    <li><strong><span class="tag">FOSTER</span> Red Ribbon Week, minimum day Friday</strong>
    — Daily dress-up themes all week; Friday is the Halloween parade and an early dismissal.</li>

Style the tag so it reads as a label, not part of the headline:
`.tag{font-family:'IBM Plex Mono',monospace; font-size:.62rem; font-weight:500;
letter-spacing:.12em; color:var(--muted); margin-right:.45rem; vertical-align:.1em}`

No source links (it is the reader's own mail) and no closing attribution
line. Order by urgency, not by school. Up to ~6 bullets across both schools;
a flat list, no sub-headers. **Omit the section entirely, header and all,
when nothing qualifies at either school** (the 🧬 Mito rule). Never pad it.

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
  Tech, Sports, San Diego, Gear up to ~8 each, Lightning & EVs up to 3, Kauai up to 2,
  School up to ~6 across both schools. These are ceilings for busy stretches, not targets. Quality
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
