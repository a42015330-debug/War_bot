# database.py

import sqlite3

from config import DATABASE_NAME


db = sqlite3.connect(
    DATABASE_NAME,
    check_same_thread=False
)

cursor = db.cursor()



cursor.execute("""
CREATE TABLE IF NOT EXISTS players(

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

missiles INTEGER,

defense INTEGER

)

""")


db.commit()



# ساخت بازیکن

def create_player(
telegram_id,
name,
country,
party
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
        ships,
        missiles,
        defense
        )

        VALUES
        (?,?,?,?,?,?,?,?,?,?,?,?)

        """,

        (

        telegram_id,
        name,
        country,
        party,

        1000,

        100000,

        100,

        0,

        0,

        0,

        0,

        50

        )

        )


        db.commit()

        return True


    except sqlite3.IntegrityError:

        return False





# گرفتن بازیکن

def get_player(telegram_id):

    cursor.execute(
    """
    SELECT * FROM players
    WHERE telegram_id=?
    """,
    (telegram_id,)
    )


    return cursor.fetchone()





# بررسی تکراری بودن اسم

def name_exists(name):

    cursor.execute(
    """
    SELECT name FROM players
    WHERE name=?
    """,
    (name,)
    )


    result = cursor.fetchone()


    return result is not None





# تغییر پول

def change_money(
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





# حذف نیرو

def update_army(
telegram_id,
field,
amount
):

    cursor.execute(
    f"""

    UPDATE players

    SET {field}=?

    WHERE telegram_id=?

    """,

    (
    amount,
    telegram_id
    )

    )


    db.commit()
