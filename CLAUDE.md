# Morning Brief — Routine Configuration
_This file is read by Claude at the start of every run. Rules here override the base prompt._

---

## Sections — Active Order

1. 🌍 WORLD
2. 🇺🇸 US & POLITICS
3. ⚡ TECH & AI
4. ✦ FAITH & THEOLOGY
5. 🌊 SAN DIEGO
6. 🎥 FILMMAKING GEAR
7. 🔋 ELECTRIC VEHICLES
8. 🧬 MITO RESEARCH

**REMOVED:** 🛠 MAKER & CREATIVE ECONOMY — dropped 2026-06-14. Section was consistently thin and low-value. Do not include it.

---

## STEP 0 — Deduplication Check (run BEFORE any content collection)

This is mandatory. It prevents the same story from repeating across consecutive briefs — a known problem in this routine.

### How to run it

```bash
bash scripts/seen-urls.sh 4 2>/dev/null
```

This outputs every article URL cited in the 4 most recent archive files. Save the output as your **SEEN_URLS blocklist**.

### How to use it

When evaluating a candidate article in STEP 3:

1. Check if its URL appears in SEEN_URLS.
2. If it does → **skip it** and log: `⚠ DEDUP [url] — already cited in recent brief`
3. If it doesn't → include it as normal.

**URL-level dedup catches exact repeats. Also apply topic-level judgment:**

- If the same underlying story (same event, same product, same study) appeared in a recent brief under a different URL, skip it *unless* there is a meaningfully new development (new facts, new outcome, not just continued coverage). Note "(developing)" in the summary if including.
- WWDC stories, ongoing product rumors, and annual reports (IEA EV Outlook, etc.) are especially prone to multi-day repetition. Be aggressive about skipping these if they ran recently.

### Exception

🧬 Mito Research: DOI URLs are per-paper and won't collide. Apply URL dedup normally. But skip a paper if you included it in a recent brief (same PMID).

### In the final report, list all DEDUP skips with reason.

---

## HTML Format — Source Attribution

Sources must be wrapped in `<span class="sources">` to display as a separate line below the story text. This is the canonical bullet format:

```html
<li>
  [1–3 sentence factual summary.]
  <span class="sources">(<a href="URL1">Source 1</a>, <a href="URL2">Source 2</a>)</span>
</li>
```

Do not put sources inline at the end of the paragraph without this wrapper. The `.sources` CSS class renders them as a distinct, smaller, muted line — which is critical for mobile readability.

---

## CSS Template

Every brief must use this `<style>` block verbatim. It is the canonical design.

```css
:root {
  --bg:         #f5f4f0;
  --surface:    #ffffff;
  --text:       #1a1a18;
  --muted:      #6b6b66;
  --rule:       #d8d7d2;
  --link:       #1a3a8f;
  --link-hover: #c41230;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  background: var(--bg);
  color: var(--text);
  font-family: 'IBM Plex Sans', sans-serif;
  font-weight: 300;
  font-size: 1.05rem;
  line-height: 1.8;
}

a {
  color: var(--link);
  text-decoration: underline;
  text-underline-offset: 2px;
  text-decoration-thickness: 1px;
}
a:hover { color: var(--link-hover); }

/* MASTHEAD */
.masthead {
  border-bottom: 2px solid var(--text);
  padding: 1.5rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  background: var(--surface);
}
.masthead-label {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.68rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--muted);
  display: block;
  margin-bottom: 0.3rem;
}
.masthead-date {
  font-family: 'IBM Plex Sans', sans-serif;
  font-weight: 300;
  font-size: 2.4rem;
  line-height: 1.05;
  color: var(--text);
}
.masthead-right {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.68rem;
  color: var(--muted);
  text-align: right;
  line-height: 1.6;
}

/* CONTENT */
.content {
  max-width: 780px;
  margin: 0 auto;
  padding: 2.5rem 2rem;
}

/* SECTION */
.section { margin-bottom: 2rem; }

.section-header {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.72rem;
  font-weight: 500;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 0.9rem;
}

ul { list-style: none; padding: 0; }

li {
  padding: 0.55rem 0 0.55rem 1.5rem;
  position: relative;
}
li::before {
  content: '—';
  position: absolute;
  left: 0;
  color: var(--muted);
}

/* SOURCE ATTRIBUTION — appears as a separate line below story text */
.sources {
  display: block;
  font-size: 0.8rem;
  color: var(--muted);
  margin-top: 0.25rem;
  line-height: 1.5;
}
.sources a {
  color: var(--muted);
  text-decoration: underline;
  text-underline-offset: 1px;
}
.sources a:hover { color: var(--link-hover); }

.section-rule {
  border: none;
  border-top: 1px solid var(--rule);
  margin: 2rem 0;
}

/* CLOSING QUOTE */
.closing-quote {
  border-top: 1px solid var(--rule);
  margin-top: 3.5rem;
  padding-top: 2.5rem;
  padding-bottom: 2rem;
  text-align: center;
}
.closing-quote blockquote {
  font-style: italic;
  font-weight: 300;
  color: var(--muted);
  font-size: 1.05rem;
  line-height: 1.85;
  max-width: 620px;
  margin: 0 auto;
}
.closing-quote cite {
  display: block;
  margin-top: 1rem;
  font-style: normal;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.72rem;
  color: var(--muted);
  letter-spacing: 0.04em;
}

/* FOOTER */
footer {
  text-align: center;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.68rem;
  color: var(--muted);
  padding: 1.5rem 2rem 3rem;
  border-top: 1px solid var(--rule);
}

/* MOBILE — optimized for iPhone reading */
@media (max-width: 600px) {
  body {
    font-size: 1.08rem;
    line-height: 1.82;
  }
  .masthead {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.4rem;
    padding: 1.1rem 1rem 1.2rem;
  }
  .masthead-right { text-align: left; }
  .masthead-date { font-size: 1.75rem; }
  .masthead-label { margin-bottom: 0.2rem; }
  .content { padding: 1.4rem 1rem; }
  .section { margin-bottom: 1.6rem; }
  .section-header {
    font-size: 0.7rem;
    margin-bottom: 0.7rem;
  }
  li {
    padding: 0.6rem 0 0.6rem 1.4rem;
  }
  .sources {
    font-size: 0.82rem;
    margin-top: 0.3rem;
  }
  .section-rule { margin: 1.6rem 0; }
  .closing-quote {
    margin-top: 2.5rem;
    padding-top: 2rem;
    padding-bottom: 1.5rem;
  }
  .closing-quote blockquote { font-size: 1rem; }
}
```
