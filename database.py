import sqlite3
from datetime import datetime

class Database():
    def __init__(self, db_name="db_weathers.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_user(self, first_name, username, chat_id):
        self.cur.execute("""
                INSERT INTO users (first_name, username, chat_id, joined_data)
                VALUES (?, ?, ?, ?)""", (first_name, username, chat_id, datetime.now()))
        self.conn.commit()

    def get_user_by_chat_id(self, chat_id):
        self.cur.execute("SELECT * FROM users WHERE chat_id = ?", (chat_id,))
        user = self.cur.fetchone()
        return user

    def close(self):
        self.conn.close()

