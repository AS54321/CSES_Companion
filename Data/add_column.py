import json
import sqlite3

# Import the files
with open("cses_problems_by_topic.json", "r") as f:
    cses = json.load(f)
conn = sqlite3.connect("cses.db")
cursor = conn.cursor()

cursor.execute('ALTER TABLE problems ADD COLUMN row_order INTEGER')
i = 0
for topic, problist in cses.items():
    i = 0
    for prob in problist:
        try:
            id = prob['id']
            cursor.execute(('UPDATE problems SET row_order=? WHERE id=?'),(i, id))
            i = i+1
        except Exception as e:
            print(f'error adding problem: {prob} owing to error {e}')

conn.commit()
conn.close()
print("Ho gya oye!")