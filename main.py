import argparse
from dashboard import run_dashboard
from crawler import crawl_targets
from keyword_monitor import monitor_keywords
from tor_client import ensure_tor, rotate_identity
import json
import os
import sys
from db import DBManager

def load_config(path='config.json'):
    if not os.path.exists(path):
        print(f"[!] Config file '{path}' not found. Please create it.")
        sys.exit(1)
    with open(path, 'r') as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="PulseScanner CLI")
    parser.add_argument('--mode', choices=['scan', 'trace', 'alert', 'dump', 'analyze', 'stealth'], default='scan')
    parser.add_argument('--keywords', type=str, help='Comma-separated keywords to monitor')
    parser.add_argument('--config', default='config.json', help='Path to config file')
    args = parser.parse_args()

    config = load_config(args.config)
    db = DBManager(config)
    ensure_tor()
    rotate_identity()

    if args.mode == 'scan':
        import threading
        stop_event = threading.Event()
        monitor_thread = threading.Thread(target=monitor_keywords, args=(config, args.keywords, stop_event), daemon=True)
        monitor_thread.start()
        try:
            run_dashboard(db)
        except KeyboardInterrupt:
            print("\nShutting down...")
            stop_event.set()
            monitor_thread.join()
    elif args.mode == 'trace':
        crawl_targets(config, db)
    # ... (other modes stubbed)
    else:
        print(f"Mode {args.mode} not yet implemented.")

if __name__ == "__main__":
    main()
