import threading
import time
from db import DBManager
import requests
from bs4 import BeautifulSoup
from webhook import send_webhook_alert

TOR_PROXIES = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

def monitor_keywords(config, keywords, stop_event=None):
    db = DBManager(config)
    kw_list = [k.strip().lower() for k in (keywords or '').split(',') if k.strip()]
    targets = config.get('targets', [])
    webhook_url = config.get('webhook_url')
    while not (stop_event and stop_event.is_set()):
        for url in targets:
            try:
                resp = requests.get(url, proxies=TOR_PROXIES, timeout=20)
                soup = BeautifulSoup(resp.text, 'html.parser')
                text = soup.get_text().lower()
                for kw in kw_list:
                    if kw and kw in text:
                        alert = f"[ALERT] Keyword '{kw}' found on {url}"
                        db.save_alert(alert)
                        print(f'[MONITOR] {alert}')
                        if webhook_url:
                            send_webhook_alert(webhook_url, alert)
            except Exception as e:
                print(f'[MONITOR] Error crawling {url}: {e}')
        time.sleep(30)
