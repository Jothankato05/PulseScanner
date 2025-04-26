import sqlite3
from cryptography.fernet import Fernet
import os

class DBManager:
    def __init__(self, config):
        self.conn = sqlite3.connect(config.get('db_path', 'pulsescanner.db'), check_same_thread=False)
        self.key = self._load_or_generate_key()
        self.fernet = Fernet(self.key)
        self._init_db()

    def _load_or_generate_key(self, key_path='key.key'):
        if os.path.exists(key_path):
            with open(key_path, 'rb') as f:
                return f.read()
        key = Fernet.generate_key()
        with open(key_path, 'wb') as f:
            f.write(key)
        return key

    def _init_db(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS alerts (id INTEGER PRIMARY KEY, alert TEXT, ts DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        c.execute('''CREATE TABLE IF NOT EXISTS raw_html (id INTEGER PRIMARY KEY, url TEXT, html BLOB, ts DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        self.conn.commit()

    def save_alert(self, alert):
        enc = self.fernet.encrypt(alert.encode())
        self.conn.execute('INSERT INTO alerts (alert) VALUES (?)', (enc,))
        self.conn.commit()

    def get_recent_alerts(self, limit=10):
        c = self.conn.cursor()
        c.execute('SELECT ts, alert FROM alerts ORDER BY ts DESC LIMIT ?', (limit,))
        rows = c.fetchall()
        alerts = []
        for ts, enc_alert in rows:
            try:
                alert = self.fernet.decrypt(enc_alert).decode()
            except Exception:
                alert = '[DECRYPTION ERROR]'
            alerts.append((ts, alert))
        return alerts
