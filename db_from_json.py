import json
import sqlite3

# Import the files
with open("cses_problems_by_topic.json", "r") as f:
    cses = json.load(f)
conn = sqlite3.connect("cses.db")
cursor = conn.cursor()

# create tables and index just in case
cursor.execute("""
    CREATE TABLE IF NOT EXISTS topics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    """)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS problems (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        url TEXT NOT NULL,
        topic_id INTEGER NOT NULL,
        is_solved INTEGER DEFAULT 0,
        notes TEXT DEFAULT '',
        FOREIGN KEY (topic_id) REFERENCES topic(id)
    )
    """)
cursor.execute('CREATE INDEX IF NOT EXISTS idx_problems_by_topic ON problems(topic_id)')

# actual script
for topic, problist in cses.items():
    cursor.execute(('INSERT OR IGNORE INTO topics (name) VALUES (?)'),(topic,))

    cursor.execute(('SELECT id FROM topics WHERE name=(?)'),(topic,))
    top_id = cursor.fetchone()[0]

    for prob in problist:
        try:
            url = prob['url']
            title = prob['title']
            id = prob['id']
            cursor.execute(('INSERT OR IGNORE INTO problems VALUES (?,?,?,?,?,?)'),(id, title, url, top_id, 0, ''))
        except Exception as e:
            print(f'error adding problem: {prob} owing to error {e}')

conn.commit()
conn.close()
print("Ho gya oye!")