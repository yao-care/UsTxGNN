#!/usr/bin/env python3
"""
US Health News Fetcher

Collects US health news from:
- Google News US Health category
- FDA News RSS
- NIH News RSS

Output: data/news/us_news.json
"""

import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import feedparser

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "news"

# Google News US Health category RSS
GOOGLE_NEWS_HEALTH_RSS = (
    "https://news.google.com/rss/topics/"
    "CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ"
    "?hl=en-US&gl=US&ceid=US:en"
)

# Google News US Science category RSS
GOOGLE_NEWS_SCIENCE_RSS = (
    "https://news.google.com/rss/topics/"
    "CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pWVXlnQVAB"
    "?hl=en-US&gl=US&ceid=US:en"
)

# FDA News RSS
FDA_NEWS_RSS = "https://www.fda.gov/about-fda/contact-fda/stay-informed/rss-feeds/fda-newsroom/rss.xml"

# NIH News RSS
NIH_NEWS_RSS = "https://www.nih.gov/news-events/news-releases/feed"

# Request delay
REQUEST_DELAY = 1.0  # seconds


def generate_id(title: str, link: str) -> str:
    """Generate news ID (hash-based on title and link)"""
    content = f"{title}:{link}"
    return hashlib.sha256(content.encode()).hexdigest()[:12]


def parse_source(entry, default_source: str = "Unknown") -> dict:
    """Extract source information from RSS entry"""
    source_name = default_source
    if hasattr(entry, "source") and hasattr(entry.source, "title"):
        source_name = entry.source.title

    return {
        "name": source_name,
        "link": entry.get("link", "")
    }


def parse_published(entry) -> str:
    """Parse published time and convert to ISO 8601 format"""
    published = entry.get("published_parsed")
    if published:
        try:
            dt = datetime(*published[:6], tzinfo=timezone.utc)
            return dt.isoformat()
        except Exception:
            pass

    # Use current time if parsing fails
    return datetime.now(timezone.utc).isoformat()


def clean_summary(summary: str) -> str:
    """Clean summary text (remove HTML tags, etc.)"""
    # Remove HTML tags
    clean = re.sub(r"<[^>]+>", "", summary)
    # Remove excess whitespace
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:500] if len(clean) > 500 else clean


def fetch_rss(url: str, source_name: str) -> list[dict]:
    """Fetch news from RSS URL"""
    print(f"  Fetching: {source_name}")
    print(f"    URL: {url[:70]}...")

    try:
        # Fetch with custom headers
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; UsTxGNN/1.0; +https://ustxgnn.yao.care)",
            "Accept": "application/rss+xml, application/xml, text/xml",
            "Accept-Language": "en-US,en;q=0.9",
        }
        request = Request(url, headers=headers)
        with urlopen(request, timeout=30) as response:
            content = response.read()
    except (HTTPError, URLError) as e:
        print(f"    Error: {e}")
        return []

    feed = feedparser.parse(content)

    if feed.bozo:
        print(f"    Warning: RSS parsing issue - {feed.bozo_exception}")

    news_items = []

    for entry in feed.entries:
        title = entry.get("title", "")
        link = entry.get("link", "")

        if not title or not link:
            continue

        news_id = generate_id(title, link)
        source = parse_source(entry, source_name)
        published = parse_published(entry)
        summary = clean_summary(entry.get("summary", "") or entry.get("description", ""))

        news_items.append({
            "id": news_id,
            "title": title,
            "published": published,
            "summary": summary,
            "sources": [source]
        })

    print(f"    Retrieved: {len(news_items)} news items")
    return news_items


def fetch_google_news_health() -> list[dict]:
    """Fetch Google News US Health category"""
    return fetch_rss(GOOGLE_NEWS_HEALTH_RSS, "Google News US Health")


def fetch_google_news_science() -> list[dict]:
    """Fetch Google News US Science category"""
    return fetch_rss(GOOGLE_NEWS_SCIENCE_RSS, "Google News US Science")


def fetch_fda_news() -> list[dict]:
    """Fetch FDA News RSS"""
    return fetch_rss(FDA_NEWS_RSS, "FDA Newsroom")


def fetch_nih_news() -> list[dict]:
    """Fetch NIH News RSS"""
    return fetch_rss(NIH_NEWS_RSS, "NIH News Releases")


def deduplicate_news(news_items: list[dict]) -> list[dict]:
    """Remove duplicate news (ID-based)"""
    seen_ids = set()
    unique_items = []

    for item in news_items:
        if item["id"] not in seen_ids:
            seen_ids.add(item["id"])
            unique_items.append(item)

    return unique_items


def filter_health_keywords(news_items: list[dict]) -> list[dict]:
    """Filter by health-related keywords"""
    health_keywords = [
        # Medical / Health general
        "medical", "medicine", "drug", "treatment", "therapy", "diagnosis",
        "surgery", "hospital", "clinic", "health", "disease", "disorder",
        "symptom", "infection", "virus", "bacteria",
        # Disease names
        "cancer", "diabetes", "hypertension", "heart", "stroke", "dementia",
        "Alzheimer", "depression", "insomnia", "asthma", "allergy",
        "hepatitis", "kidney", "liver", "lung", "brain",
        # Drugs / Treatments
        "FDA", "approval", "clinical trial", "vaccine", "antibody",
        "immunotherapy", "gene therapy", "stem cell", "regenerative",
        # Research
        "research", "discovery", "development", "efficacy", "side effect",
        "risk", "study", "breakthrough", "trial",
        # Pharmaceutical
        "pharmaceutical", "biotech", "biotechnology", "drugmaker",
    ]

    filtered = []
    for item in news_items:
        text = f"{item['title']} {item.get('summary', '')}".lower()
        if any(keyword.lower() in text for keyword in health_keywords):
            filtered.append(item)

    return filtered


def main():
    print("Collecting US health news...")

    # Ensure directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    all_news = []

    # Google News US Health
    news = fetch_google_news_health()
    all_news.extend(news)
    time.sleep(REQUEST_DELAY)

    # Google News US Science
    news = fetch_google_news_science()
    all_news.extend(news)
    time.sleep(REQUEST_DELAY)

    # FDA News
    news = fetch_fda_news()
    all_news.extend(news)
    time.sleep(REQUEST_DELAY)

    # NIH News
    news = fetch_nih_news()
    all_news.extend(news)

    # Deduplicate
    unique_news = deduplicate_news(all_news)
    print(f"\nAfter deduplication: {len(unique_news)} items")

    # Health-related filtering
    health_news = filter_health_keywords(unique_news)
    print(f"After health filtering: {len(health_news)} items")

    # Sort by published date (newest first)
    health_news.sort(key=lambda x: x["published"], reverse=True)

    # Output
    output = {
        "source": "us_news",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "total_fetched": len(all_news),
        "unique_count": len(unique_news),
        "health_related_count": len(health_news),
        "news": health_news
    }

    output_path = DATA_DIR / "us_news.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nOutput: {output_path}")
    print(f"  - Total fetched: {len(all_news)}")
    print(f"  - Unique: {len(unique_news)}")
    print(f"  - Health-related: {len(health_news)}")


if __name__ == "__main__":
    main()
