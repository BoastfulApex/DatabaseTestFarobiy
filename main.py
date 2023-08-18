import sqlite3

conn = sqlite3.connect('my.db')

cur = conn.cursor()

command = '''SELECT user_id, lang FROM USERS WHERE NOT lang="uzb";'''

cur.execute(command)

result = cur.fetchall()

print(result)
