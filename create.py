import sqlite3

db = sqlite3.connect('posts.db')

cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS posts (user TEXT, profile TEXT, url TEXT, title TEXT)""")


db.commit()