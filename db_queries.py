import sqlite3


conn = sqlite3.connect('cses.db')
cursor = conn.cursor()


def fetch_topics():
    cursor.execute('SELECT * FROM topics')
    return cursor.fetchall()

def fetch_problems(tid):
    cursor.execute('SELECT * FROM problems WHERE topic_id=?',(tid,))
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