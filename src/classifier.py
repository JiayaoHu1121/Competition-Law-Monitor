import re
from config import load_config

config = load_config()

def classify_category(title, summary):
    text = (title + " " + summary).lower()
    if any(k in text for k in ["law", "legislation", "regulation", "directive", "act"]):
        return "legislation"
    elif any(k in text for k in ["sanction", "fine", "penalty", "enforcement", "investigation", "cartel"]):
        return "sanctions_and_suppression_actions"
    else:
        return "research_reports_public_opinion"

def get_level(title, summary):
    text = (title + " " + summary).lower()
    if any(kw.lower() in text for kw in config["chinese_keywords"]):
        return "最高级别（涉及中国企业）"
    # 中等级别：大公司或全球关键词
    global_keywords = ["google", "apple", "amazon", "meta", "microsoft", "global", "international"]
    if any(k in text for k in global_keywords):
        return "中等级别（全球影响力）"
    return "低级别（当地境内）"
