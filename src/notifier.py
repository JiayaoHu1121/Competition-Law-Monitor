import requests
import json
from datetime import datetime

def send_to_feishu(events):
    if not events:
        return
    message = {
        "msg_type": "text",
        "content": {
            "text": f"【竞争法监控日报】\n北京时间 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n" +
                    "\n\n".join([
                        f"【{e['level']}】{e['category']}\n{e['title']}\n来源: {e['link']}" 
                        for e in events
                    ])
        }
    }
    webhook = load_config()["feishu_webhook"]
    requests.post(webhook, json=message)
