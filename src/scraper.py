import feedparser
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import pytz

def fetch_rss(url):
    feed = feedparser.parse(url)
    items = []
    for entry in feed.entries[:10]:  # 限制数量
        items.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.get("published", entry.get("updated")),
            "summary": entry.get("summary", ""),
            "source": url
        })
    return items

def scrape_accc():  # 示例补充非RSS
    # ACCC 官网可扩展为 BeautifulSoup，这里简化
    return []

def get_all_sources():
    sources = {
        "EU": [
            "https://eur-lex.europa.eu/rss?locale=en",  # EUR-Lex
            # 添加更多 competition 特定 RSS
        ],
        "US": [
            "https://www.ftc.gov/feeds/press-release-competition.xml",
            "https://www.justice.gov/atr/news-feeds",  # DOJ
        ],
        "AU": [
            "https://www.accc.gov.au/media-releases/rss",  # 如有，替换实际
        ]
    }
    all_items = []
    for region, urls in sources.items():
        for url in urls:
            try:
                items = fetch_rss(url)
                for item in items:
                    item["region"] = region
                all_items.extend(items)
            except:
                pass
    return all_items
