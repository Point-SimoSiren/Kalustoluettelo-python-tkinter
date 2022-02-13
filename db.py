import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor
        self.cur.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, \
        price text, timebought text, shop text, borrowedby text, timeborrowed text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM items")
        rows = self.cur.fetchall()
        return rows
    
    def insert(self, name, price, timebought, shop, borrowedby, timeborrowed):
        self.cur.execute("INSERT INTO items VALUES (NULL, ?, ?, ?, ?, ?, ?)")