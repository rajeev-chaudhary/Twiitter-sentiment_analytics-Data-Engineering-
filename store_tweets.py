import sqlite3
from tweet_stream import get_stream

# Connect DB
conn = sqlite3.connect("tweets.db")
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS tweets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    text TEXT,
    sentiment INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

# Stream & insert
for tweet in get_stream():
    cur.execute("INSERT INTO tweets (user, text, sentiment) VALUES (?, ?, ?)",
                (tweet["user"], tweet["text"], tweet["sentiment"]))
    conn.commit()
    print("Inserted:", tweet)
