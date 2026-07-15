from config import load_config

config = load_config()

def classify_category(title, summary):
    text = (title + " " + summary).lower()
    if any(k in text for k in ["law", "legislation", "regulation", "directive", "act", "法案", "条例"]):
        return "legislation"
    elif any(k in text for k in ["sanction", "fine", "penalty", "enforcement", "investigation", "cartel", "罚款", "调查"]):
        return "sanctions_and_suppression_actions"
    else:
        return "research_reports_public_opinion"

def get_level(title, summary):
    text = (title + " " + summary).lower()
    if any(kw.lower() in text for kw in config.get("chinese_keywords", [])):
        return "最高级别（涉及中国企业）"
    global_keywords = ["google", "apple", "amazon", "meta", "microsoft", "global", "international", "欧盟", "美国", "澳洲"]
    if any(k in text for k in global_keywords):
        return "中等级别（全球影响力）"
    return "低级别（当地境内）"
