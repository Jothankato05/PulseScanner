#!/bin/bash
set -e

# Create venv if not exists
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Copy example config if needed
if [ ! -f config.json ]; then
  cp config.example.json config.json
  echo "[INFO] config.json created. Please edit it with your targets and webhook URL."
fi

# Guide for Tor
if ! command -v tor >/dev/null; then
  echo "[WARNING] Tor is not installed. Install with: sudo apt install tor"
else
  echo "[INFO] Ensure Tor is running: sudo service tor start"
fi

echo "[SETUP COMPLETE] Activate venv with 'source venv/bin/activate' and run './run.sh --keywords \"brand1,brand2\"'"
