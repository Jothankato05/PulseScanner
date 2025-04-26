import requests
import json

def send_webhook_alert(webhook_url, alert):
    """Send an alert to a webhook endpoint (Discord, Slack, SIEM, etc)."""
    if not webhook_url:
        return
    data = {"text": alert}
    try:
        resp = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'}, timeout=10)
        if resp.status_code not in (200, 204):
            print(f"[WEBHOOK] Failed to send alert: {resp.status_code} {resp.text}")
    except Exception as e:
        print(f"[WEBHOOK] Error: {e}")
