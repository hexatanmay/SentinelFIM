from datetime import datetime
from database import Database

db = Database()


class Logger:
    @staticmethod
    def log(event_type, details):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = f"[{timestamp}] [{event_type}] {details}"

        print(log_entry)

        with open("activity.log", "a", encoding="utf-8") as file:
            file.write(log_entry + "\n")

        db.insert_event(
            timestamp,
            event_type,
            details
        )
        
