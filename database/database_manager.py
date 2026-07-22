import sqlite3


class DatabaseManager:

    def __init__(self):
        self.connection = sqlite3.connect("sonam_creator_ai.db")
        self.cursor = self.connection.cursor()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT,
            value TEXT
        )
        """)

        self.connection.commit()

        print("[✓] Database Ready")