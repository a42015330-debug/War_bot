import sqlite3

db = sqlite3.connect("worldwar.db", check_same_thread=False)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS players(

user_id INTEGER PRIMARY KEY,

country TEXT,

money INTEGER,

oil INTEGER,

steel INTEGER,

food INTEGER,

army INTEGER,

airforce INTEGER,

navy INTEGER,

missiles INTEGER,

defense INTEGER,

wins INTEGER,

level INTEGER

)
""")

db.commit()
