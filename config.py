import json
import os

def load_config():
    # 优先使用环境变量（GitHub Actions 使用）
    if os.getenv("FEISHU_WEBHOOK"):
        return {
            "feishu_webhook": os.getenv("FEISHU_WEBHOOK"),
            "chinese_keywords": ["华为", "Huawei", "中兴", "ZTE", "比亚迪", "BYD", "阿里巴巴", "Alibaba", "腾讯", "Tencent", "中国企业", "中国公司"],
            "max_items_per_day": 10
        }
    
    # 本地使用 config.json
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("警告：未找到 config.json，使用默认配置")
        return {
            "feishu_webhook": "",
            "chinese_keywords": ["华为", "Huawei", "中兴", "ZTE", "比亚迪", "BYD", "阿里巴巴", "Alibaba", "腾讯", "Tencent", "中国企业", "中国公司"],
            "max_items_per_day": 10
        }
