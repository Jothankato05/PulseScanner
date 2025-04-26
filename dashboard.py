from rich.console import Console
from rich.live import Live
from rich.table import Table
import time

def run_dashboard(db):
    console = Console()
    with Live(refresh_per_second=2) as live:
        while True:
            table = Table(title="PulseScanner Alerts")
            table.add_column("Time")
            table.add_column("Alert")
            # Fetch recent alerts from db
            alerts = db.get_recent_alerts(10)
            if alerts:
                for ts, alert in alerts:
                    table.add_row(str(ts), alert)
            else:
                table.add_row("-", "No alerts yet.")
            live.update(table)
            time.sleep(2)
