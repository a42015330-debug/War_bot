# database.py

import sqlite3
from config import DATABASE_NAME


db = sqlite3.connect(
    DATABASE_NAME,
    check_same_thread=False
)

cursor = db.cursor()


# ساخت جدول بازیکنان

cursor.execute("""
CREATE TABLE IF NOT EXISTS players (

    id INTEGER PRIMARY KEY,

    telegram_id INTEGER UNIQUE,

    name TEXT UNIQUE,

    country TEXT,

    party TEXT,

    money INTEGER,

    population INTEGER,

    soldiers INTEGER,

    tanks INTEGER,

    planes INTEGER,

    ships INTEGER,

    oil INTEGER DEFAULT 0,

    gold INTEGER DEFAULT 0,

    iron INTEGER DEFAULT 0

)
""")


db.commit()



# ساخت بازیکن جدید

def create_player(
        telegram_id,
        name,
        country,
        party,
        money,
        population,
        soldiers,
        tanks,
        planes,
        ships
):

    try:

        cursor.execute(
        """
        INSERT INTO players
        (
        telegram_id,
        name,
        country,
        party,
        money,
        population,
        soldiers,
        tanks,
        planes,
        ships
        )

        VALUES (?,?,?,?,?,?,?,?,?,?)

        """,
        (
        telegram_id,
        name,
        country,
        party,
        money,
        population,
        soldiers,
        tanks,
        planes,
        ships
        )
        )


        db.commit()

        return True


    except sqlite3.IntegrityError:

        return False




# گرفتن اطلاعات بازیکن

def get_player(telegram_id):

    cursor.execute(
    "SELECT * FROM players WHERE telegram_id=?",
    (telegram_id,)
    )

    return cursor.fetchone()



# بررسی تکراری بودن اسم

def check_name(name):

    cursor.execute(
    "SELECT name FROM players WHERE name=?",
    (name,)
    )

    result = cursor.fetchone()


    if result:
        return False

    return True



# تغییر پول

def update_money(
        telegram_id,
        amount
):

    cursor.execute(
    """
    UPDATE players
    SET money = money + ?
    WHERE telegram_id=?
    """,
    (
    amount,
    telegram_id
    )
    )

    db.commit()
