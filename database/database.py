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
                file_path TEXT,
                risk_score INTEGER,
                severity TEXT,
                details TEXT
            )
        """)
        self.conn.commit()

    def insert_event(
        self,
        timestamp,
        event_type,
        file_path,
        risk_score,
        severity,
        details
    ):
        self.cursor.execute(
            """
            INSERT INTO events(
                timestamp,
                event_type,
                file_path,
                risk_score,
                severity,
                details
            )
            VALUES(?,?,?,?,?,?)
            """,
            (
                timestamp,
                event_type,
                file_path,
                risk_score,
                severity,
                details
            )
        )

        self.conn.commit()

    def get_events(self):
        self.cursor.execute(
            """
            SELECT *
            FROM events
            ORDER BY id DESC
            """
        )

        return self.cursor.fetchall()

    def get_high_risk_events(self):
        self.cursor.execute(
            """
            SELECT *
            FROM events
            WHERE risk_score >= 70
            ORDER BY id DESC
            """
        )

        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
