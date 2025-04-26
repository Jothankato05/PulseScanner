# PulseScanner

## About
PulseScanner is a modular, passive OSINT engine designed for real-time monitoring of dark web and deep web onion services. It enables security teams, researchers, and organizations to:
- Monitor multiple .onion sites via Tor
- Detect and alert on custom keywords in real time
- Display findings in a live dashboard and send alerts to webhooks (Discord, Slack, SIEM, etc)
- Store alerts securely in an encrypted local database
- Easily extend or integrate with other tools

PulseScanner is ideal for threat intelligence, brand protection, and security research, with a focus on privacy, modularity, and automation.

---

## 🚀 Features
- Monitors dark web forums, markets, and leak hubs for new posts, leaks, and keywords
- CLI dashboard with real-time alerts (using `rich`)
- All traffic routed through Tor for anonymity
- Encrypted logging (with `cryptography`)
- SQLite (default) or MongoDB storage
- Modular architecture for easy expansion
- Passive-only: no login, no interaction, no transactions
- Compliance-focused: for research and enterprise defense only

---

## 🚀 Quick Setup

```bash
# Python 3.10+ recommended
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the CLI
python main.py --mode scan --keywords "brand1,brand2"
```

---

## ⚙️ Modes
- `scan`: Watchlist keyword scanning
- `trace`: Full onion crawl (limited depth)
- `alert`: Trigger on keywords/entity tags
- `dump`: Save & encrypt raw HTML + metadata
- `analyze`: AI/NER extraction (optional)
- `stealth`: Rotating identities, delays, human-like patterns

---

## 📦 Output Channels
- CLI dashboard (default)
- Webhook integration (SIEM, Discord, Slack)
- Encrypted logs

---

## 🔒 Compliance & Ethics
PulseScanner is a **passive-only recon tool**. It does not interact, login, or purchase. Intended for legal, ethical research and defense.

---

## 🧩 Architecture

```
[CLI Input] ---> [Keyword Monitor Engine] ---> [Dark Web Crawlers (via Tor)]
                                    ↓
                        [Signal Processing Layer]
                                    ↓
                         [Alert System + Logs]
```

---

## 📚 License & Disclaimer
All rights reserved. For legal, ethical research only. See LICENSE for details.
