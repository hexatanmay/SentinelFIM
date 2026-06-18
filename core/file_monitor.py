from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class FileMonitorHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"[CREATED] {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory:
            print(f"[MODIFIED] {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"[DELETED] {event.src_path}")

    def on_moved(self, event):
        if not event.is_directory:
            print(f"[MOVED] {event.src_path} -> {event.dest_path}")


class FileMonitor:
    def __init__(self, path):
        self.path = path
        self.observer = Observer()

    def start(self):
        event_handler = FileMonitorHandler()
        self.observer.schedule(event_handler, self.path, recursive=True)
        self.observer.start()

        print(f"[INFO] Monitoring started on: {self.path}")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.observer.stop()
        self.observer.join()
        print("[INFO] Monitoring stopped")
