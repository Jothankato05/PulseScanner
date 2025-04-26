import requests
from bs4 import BeautifulSoup
from tor_client import ensure_tor

def crawl_targets(config, db):
    targets = config.get('targets', [])
    for url in targets:
        try:
            print(f'[CRAWL] {url}')
            resp = requests.get(url, proxies={
                'http': 'socks5h://127.0.0.1:9050',
                'https': 'socks5h://127.0.0.1:9050'
            }, timeout=20)
            soup = BeautifulSoup(resp.text, 'html.parser')
            db.save_raw(url, resp.text)
        except Exception as e:
            print(f'[!] Failed to crawl {url}: {e}')
