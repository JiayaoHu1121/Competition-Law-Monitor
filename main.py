from src.scraper import get_all_sources
from src.classifier import classify_category, get_level
from src.notifier import send_to_feishu
import json
from datetime import datetime

def main():
    items = get_all_sources()
    events = []
    for item in items:
        category = classify_category(item["title"], item["summary"])
        level = get_level(item["title"], item["summary"])
        events.append({
            "title": item["title"],
            "link": item["link"],
            "category": category,
            "level": level,
            "region": item["region"],
            "time": item["published"]
        })
    
    # 简单去重（可扩展 SQLite）
    send_to_feishu(events[:10])  # 限制条数

if __name__ == "__main__":
    main()
