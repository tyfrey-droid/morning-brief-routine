#!/usr/bin/env python3
"""Step 1: Fetch anchor RSS feeds and save to articles.json — stdlib only"""

import socket
socket.setdefaulttimeout(10)

import json
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from html.parser import HTMLParser
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

LOOKBACK_HOURS = 28
NOW = datetime.now(timezone.utc)
CUTOFF = NOW - timedelta(hours=LOOKBACK_HOURS)


class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, data):
        self.text.append(data)

    def get_data(self):
        return " ".join(self.text)


def strip_html(raw):
    if not raw:
        return ""
    s = HTMLStripper()
    try:
        s.feed(raw)
        return re.sub(r'\s+', ' ', s.get_data()).strip()
    except Exception:
        return re.sub(r'<[^>]+>', '', str(raw)).strip()


def parse_date_str(date_str):
    if not date_str:
        return None
    date_str = date_str.strip()
    # Try RFC 2822 (RSS)
    try:
        return parsedate_to_datetime(date_str).astimezone(timezone.utc)
    except Exception:
        pass
    # Try ISO 8601 / Atom
    for fmt in (
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S.%f%z",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%d",
    ):
        try:
            dt = datetime.strptime(date_str[:len(fmt)+5], fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except Exception:
            pass
    return None


def fetch_url(url):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "MorningBrief/1.0 (+automated-news-reader)"}
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.read()


def ns(tag, namespace):
    return f"{{{namespace}}}{tag}"


def parse_rss_atom(content, source_name):
    """Parse RSS 2.0, RSS 1.0, or Atom feeds. Returns list of dicts."""
    articles = []
    try:
        # Strip BOM / leading whitespace
        if isinstance(content, bytes):
            content = content.lstrip(b'\xef\xbb\xbf')
        root = ET.fromstring(content)
    except ET.ParseError as e:
        print(f"    XML parse error: {e}")
        return articles

    tag = root.tag.lower()

    # Atom feed
    atom_ns = "http://www.w3.org/2005/Atom"
    if "atom" in tag or root.tag == f"{{{atom_ns}}}feed":
        for entry in root.findall(f"{{{atom_ns}}}entry"):
            title_el = entry.find(f"{{{atom_ns}}}title")
            title = strip_html(title_el.text if title_el is not None else "")

            link_el = entry.find(f"{{{atom_ns}}}link[@rel='alternate']")
            if link_el is None:
                link_el = entry.find(f"{{{atom_ns}}}link")
            url_ = (link_el.get("href", "") if link_el is not None else "")

            summary_el = entry.find(f"{{{atom_ns}}}summary") or entry.find(f"{{{atom_ns}}}content")
            summary = strip_html(summary_el.text if summary_el is not None else "")

            date_el = entry.find(f"{{{atom_ns}}}published") or entry.find(f"{{{atom_ns}}}updated")
            date_str = date_el.text if date_el is not None else ""
            date = parse_date_str(date_str) or NOW

            if title:
                articles.append({
                    "title": title, "url": url_, "source": source_name,
                    "snippet": summary[:300], "date": date, "is_anchor": True
                })
        return articles

    # RSS 2.0 / 1.0
    # Find channel items
    channel = root.find("channel")
    if channel is None:
        channel = root  # RSS 1.0 puts items at root level

    # RSS 1.0 namespace
    rss1_ns = "http://purl.org/rss/1.0/"
    items = channel.findall("item")
    if not items:
        items = root.findall(f"{{{rss1_ns}}}item")
    if not items:
        items = root.findall("item")

    for item in items:
        def get_text(tag_name):
            el = item.find(tag_name)
            if el is not None and el.text:
                return el.text
            # Try with RSS 1.0 ns
            el = item.find(f"{{{rss1_ns}}}{tag_name}")
            if el is not None and el.text:
                return el.text
            return ""

        title = strip_html(get_text("title"))
        url_ = get_text("link") or get_text("guid")
        # Some feeds put URL in link with text
        link_el = item.find("link")
        if link_el is not None:
            url_ = (link_el.text or "").strip() or url_

        summary = strip_html(get_text("description") or get_text("summary"))
        # Try content:encoded
        content_ns = "http://purl.org/rss/1.0/modules/content/"
        content_el = item.find(f"{{{content_ns}}}encoded")
        if content_el is not None and content_el.text:
            summary = strip_html(content_el.text)

        date_str = get_text("pubDate") or get_text("dc:date") or get_text("date")
        # Try dc namespace
        dc_ns = "http://purl.org/dc/elements/1.1/"
        dc_el = item.find(f"{{{dc_ns}}}date")
        if dc_el is not None and dc_el.text:
            date_str = dc_el.text

        date = parse_date_str(date_str) or NOW

        if title:
            articles.append({
                "title": title, "url": url_, "source": source_name,
                "snippet": summary[:300], "date": date, "is_anchor": True
            })

    return articles


def fetch_section(section):
    seen_titles = set()
    articles = []

    for source_name, url in section["feeds"]:
        print(f"  Fetching {source_name}...")
        try:
            content = fetch_url(url)
            items = parse_rss_atom(content, source_name)
        except Exception as e:
            print(f"  WARN: {source_name} ({url}) — {e}")
            continue

        for art in items:
            title_key = re.sub(r'\s+', ' ', art["title"].lower().strip())
            if title_key in seen_titles or not title_key:
                continue

            date = art["date"]
            if isinstance(date, str):
                date = parse_date_str(date) or NOW

            if date < CUTOFF:
                continue

            # Keyword filter
            combined = f"{art['title']} {art['snippet']}"
            if section["keywords"] and not any(
                kw.lower() in combined.lower() for kw in section["keywords"]
            ):
                continue

            seen_titles.add(title_key)
            art["date"] = date.isoformat()
            articles.append(art)

    articles.sort(key=lambda a: a["date"], reverse=True)
    articles = articles[:section["max_items"]]

    print(f"  → {section['emoji']} {section['title']}: {len(articles)} articles")
    return articles


SECTIONS = [
    {
        "id": "world", "emoji": "🌍", "title": "World",
        "max_items": 8, "keywords": [],
        "feeds": [
            ("Reuters Top News", "https://feeds.reuters.com/reuters/topNews"),
            ("BBC World", "http://feeds.bbci.co.uk/news/world/rss.xml"),
            ("AP News", "https://apnews.com/rss"),
        ]
    },
    {
        "id": "us_politics", "emoji": "🇺🇸", "title": "US & Politics",
        "max_items": 8, "keywords": [],
        "feeds": [
            ("Reuters Politics", "https://feeds.reuters.com/Reuters/PoliticsNews"),
            ("NPR Politics", "https://feeds.npr.org/1014/rss.xml"),
            ("BBC US & Canada", "http://feeds.bbci.co.uk/news/world/us-canada/rss.xml"),
        ]
    },
    {
        "id": "tech_ai", "emoji": "⚡", "title": "Tech & AI",
        "max_items": 8, "keywords": [],
        "feeds": [
            ("Ars Technica", "http://feeds.arstechnica.com/arstechnica/index"),
            ("MIT Technology Review", "https://www.technologyreview.com/feed/"),
            ("The Verge", "https://www.theverge.com/rss/index.xml"),
            ("512 Pixels", "https://512pixels.net/feed/"),
        ]
    },
    {
        "id": "faith_theology", "emoji": "✦", "title": "Faith & Theology",
        "max_items": 2, "keywords": [],
        "feeds": [
            ("Christianity Today", "https://www.christianitytoday.com/ct/feeds/all/"),
            ("Religion News Service", "https://religionnews.com/feed/"),
            ("Gospel Coalition", "https://www.thegospelcoalition.org/feed/"),
        ]
    },
    {
        "id": "san_diego", "emoji": "🌊", "title": "San Diego",
        "max_items": 8, "keywords": [],
        "feeds": [
            ("KPBS", "https://www.kpbs.org/rss2/news/"),
            ("Voice of San Diego", "https://voiceofsandiego.org/feed/"),
        ]
    },
    {
        "id": "maker", "emoji": "🛠", "title": "Maker & Creative Economy",
        "max_items": 8, "keywords": [],
        "feeds": [
            ("Make Magazine", "https://makezine.com/feed/"),
            ("Colossal", "https://www.thisiscolossal.com/feed/"),
        ]
    },
    {
        "id": "filmmaking", "emoji": "🎥", "title": "Filmmaking Gear",
        "max_items": 8,
        "keywords": [
            "sony", "fx6", "e-mount", "emount", "smallhd", "ronin 4d",
            "dji ronin", "cinema lens", "fe lens", "g master", "sigma cine",
            "gimbal", "matte box", "follow focus", "firmware update",
            "mirrorless cinema", "video camera", "cine lens", "lens review"
        ],
        "feeds": [
            ("News Shooter", "https://www.newsshooter.com/feed/"),
            ("CineD", "https://www.cined.com/feed/"),
            ("Alister Chapman", "https://www.xdcam-user.com/alisters-blog/feed/"),
            ("cinema5D", "https://www.cinema5d.com/feed/"),
        ]
    },
    {
        "id": "mito_research", "emoji": "🧬", "title": "Mito Research",
        "max_items": 8,
        "keywords": [
            "melas", "mitochondrial", "mitochondria", "heteroplasmy", "m.3243",
            "mtdna", "gene therapy", "stroke-like", "lactic acidosis",
            "encephalomyopathy", "seizure", "neuroprotection", "rare disease"
        ],
        "feeds": [
            ("PubMed MELAS", "https://pubmed.ncbi.nlm.nih.gov/rss/search/?term=MELAS+mitochondrial&format=rss"),
            ("PubMed Mito", "https://pubmed.ncbi.nlm.nih.gov/rss/search/?term=mitochondrial+disease+treatment&format=rss"),
            ("NIH News", "https://www.nih.gov/feeds/news.xml"),
            ("NORD", "https://rarediseases.org/feed/"),
        ]
    },
    {
        "id": "ev", "emoji": "🔋", "title": "Electric Vehicles",
        "max_items": 8, "keywords": [],
        "feeds": [
            ("Electrek", "https://electrek.co/feed/"),
            ("InsideEVs", "https://insideevs.com/rss/articles/"),
        ]
    },
]


def main():
    print(f"Morning Brief fetch — {NOW.strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"Lookback: {LOOKBACK_HOURS}h (cutoff: {CUTOFF.strftime('%Y-%m-%d %H:%M UTC')})")
    print()

    sections_out = []
    for sec in SECTIONS:
        print(f"[{sec['emoji']} {sec['title']}]")
        anchor_articles = fetch_section(sec)
        sections_out.append({
            "id": sec["id"],
            "emoji": sec["emoji"],
            "title": sec["title"],
            "editorial": "",
            "anchor_articles": anchor_articles,
            "expanded_articles": []
        })
        print()

    output = {
        "generated": NOW.isoformat(),
        "sections": sections_out
    }

    with open("articles.json", "w") as f:
        json.dump(output, f, indent=2)

    print("Saved to articles.json")


if __name__ == "__main__":
    main()
