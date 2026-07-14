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

It runs on a schedule at 12:15 & 13:00 UTC (5:15 & 6:00 AM PT) before the
morning brief. Each run:

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
  San Diego · 🌺 Kauai (max 2) · Filmmaking Gear · Weather · Surf ·
  One Good Thing · On This Day (exactly 1 item) · closing quote.
- No Electric Vehicles section (removed 2026-07-13 by reader request).
