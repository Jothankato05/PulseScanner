import requests
from stem import Signal
from stem.control import Controller
import time

def ensure_tor(port=9050):
    # Simple check for Tor SOCKS proxy
    try:
        r = requests.get('http://check.torproject.org', proxies={
            'http': f'socks5h://127.0.0.1:{port}',
            'https': f'socks5h://127.0.0.1:{port}'
        }, timeout=10)
        if 'Congratulations. This browser is configured to use Tor.' in r.text:
            print('[+] Tor connection OK')
        else:
            print('[!] Tor may not be running or configured.')
    except Exception as e:
        print(f'[!] Tor connection failed: {e}')

def rotate_identity(control_port=9051, password=None):
    try:
        with Controller.from_port(port=control_port) as controller:
            controller.authenticate(password=password)
            controller.signal(Signal.NEWNYM)
            print('[*] Tor identity rotated.')
            time.sleep(3)
    except Exception as e:
        print(f'[!] Failed to rotate Tor identity: {e}')
