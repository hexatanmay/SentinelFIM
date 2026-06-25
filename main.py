from watchdog.observers import Observer
from core.watchdog_handler import SentinelHandler

import time

WATCH_PATH = "monitored"

observer = Observer()
handler = SentinelHandler()

observer.schedule(
    handler,
    WATCH_PATH,
    recursive=True
)

observer.start()

print(f"Monitoring: {WATCH_PATH}")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()