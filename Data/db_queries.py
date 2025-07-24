import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "cses.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


def fetch_topics():
    cursor.execute('SELECT * FROM topics')
    return cursor.fetchall()

''''
pid, title, url, sol

CREATE TABLE IF NOT EXISTS problems (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        url TEXT NOT NULL,
        topic_id INTEGER NOT NULL,
        is_solved INTEGER DEFAULT 0,
        notes TEXT DEFAULT '',
        FOREIGN KEY (topic_id) REFERENCES topic(id)
    )
    '''


def fetch_problems(tid):
    cursor.execute('SELECT id, title, url, is_solved FROM problems WHERE topic_id=? ORDER BY row_order;',(tid,))
    return cursor.fetchall()

def db_toggle_prob(pid):
    cursor.execute('UPDATE problems SET is_solved = NOT is_solved WHERE id = ?',(pid,))

def fetch_notes(pid):
    cursor.execute('SELECT notes FROM problems WHERE id = ?', (pid,))
    return cursor.fetchone()[0]

def db_update_notes(content, pid):
    cursor.execute('UPDATE problems SET notes=? WHERE id = ?',(content, pid))

def close_db():
    conn.commit()
    conn.close()

def check_notes(pid):
    cursor.execute('SELECT notes FROM problems WHERE id = ?', (pid,))
    return ''==cursor.fetchone()[0]

def fetch_random(tids):
    placeholder = ','.join(['?']*len(tids))
    cursor.execute(f'''SELECT id, title, url, is_solved FROM problems WHERE topic_id IN ({placeholder}) AND is_solved=0
                    ORDER BY RANDOM()
                    LIMIT 10
                   ''',tids)
    return cursor.fetchall()