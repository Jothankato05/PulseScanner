import json

def load_config(path='config.json'):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        # Default config
        return {
            'db_path': 'pulsescanner.db',
            'targets': [
                'http://dread.onion',
                'http://darknetlive.onion',
                'http://exodus.onion'
            ]
        }
