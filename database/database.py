import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("activity.db")
        self.cursor = self.conn.cursor()

        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS events(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                event_type TEXT,
                details TEXT
            )
        """)
        self.conn.commit()

    def insert_event(self, timestamp, event_type, details):
        self.cursor.execute(
            """
            INSERT INTO events(timestamp,event_type,details)
            VALUES(?,?,?)
            """,
            (timestamp, event_type, details)
        )
        self.conn.commit()

    def get_events(self):
        self.cursor.execute("SELECT * FROM events")
        return self.cursor.fetchall()
