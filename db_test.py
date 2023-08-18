import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()
query = '''SELECT * FROM TelegramUser;'''
cursor.execute(query)

result = cursor.fetchall()

print(result)
