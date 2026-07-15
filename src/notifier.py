import requests
from datetime import datetime
from config import load_config

def send_to_feishu(events):
    config = load_config()
    webhook = config.get("feishu_webhook")
    if not webhook:
        print("未配置飞书 webhook")
        return

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    if not events:
        text = f"【竞争法监控日报】\n北京时间 {now}\n\n今日暂无新动态。"
    else:
        text = f"【竞争法监控日报】\n北京时间 {now}\n\n" + "\n\n".join([
            f"【{e['level']}】{e['category']}\n{e['title']}\n🔗 {e['link']}" 
            for e in events[:config.get("max_items_per_day", 10)]
        ])

    message = {
        "msg_type": "text",
        "content": {"text": text}
    }
    
    try:
        resp = requests.post(webhook, json=message, timeout=10)
        print(f"飞书推送状态: {resp.status_code}")
    except Exception as e:
        print(f"推送失败: {e}")
