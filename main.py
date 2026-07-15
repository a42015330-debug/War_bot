import random

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from config import BOT_TOKEN
from database import cursor, db
from countries import COUNTRIES


# ---------- ساخت بازیکن ----------

def create_player(user_id):

    country = random.choice(list(COUNTRIES.keys()))

    info = COUNTRIES[country]

    cursor.execute(
        """
        INSERT INTO players
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,
        (
            user_id,
            country,
            info["money"],
            info["oil"],
            info["steel"],
            info["food"],
            info["army"],
            info["airforce"],
            info["navy"],
            info["missiles"],
            info["defense"],
            0,
            1,
        ),
    )

    db.commit()


# ---------- شروع ----------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user.id

    cursor.execute(
        "SELECT * FROM players WHERE user_id=?",
        (user,),
    )

    player = cursor.fetchone()

    if player is None:
        create_player(user)

    await update.message.reply_text(
        """
🌍 به بازی جنگ جهانی خوش آمدید

دستورها:

/status
/economy
/military
/attack
/shop
/help
"""
    )


# ---------- وضعیت ----------

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user.id

    cursor.execute(
        "SELECT * FROM players WHERE user_id=?",
        (user,),
    )

    p = cursor.fetchone()

    if p is None:

        await update.message.reply_text(
            "اول /start را بزن."
        )

        return

    text = f"""
🌍 کشور : {p[1]}

💰 پول : {p[2]}

🛢 نفت : {p[3]}

🔩 فولاد : {p[4]}

🌾 غذا : {p[5]}

🪖 ارتش : {p[6]}

✈️ نیروی هوایی : {p[7]}

🚢 نیروی دریایی : {p[8]}

🚀 موشک : {p[9]}

🛡 دفاع : {p[10]}

🏆 برد : {p[11]}

⭐ سطح : {p[12]}
"""

    await update.message.reply_text(text)


# ---------- اقتصاد ----------

async def economy(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """
🏭 بخش اقتصاد

به زودی:

🛢 استخراج نفت

🏭 کارخانه

⛏ معدن

💵 مالیات

🏦 بانک

📈 درآمد
"""
    )


# ---------- ارتش ----------

async def military(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        """
🪖 بخش نظامی

به زودی:

🚜 تانک

✈️ جنگنده

🚁 هلیکوپتر

🚢 ناو

🚀 موشک

🛡 پدافند
"""
    )


# ---------- حمله ----------

async def attack(update: Update, context: ContextTypes.DEFAULT_TYPE):

    power = random.randint(1, 100)

    if power > 50:

        result = "✅ حمله موفق بود."

    else:

        result = "❌ حمله شکست خورد."

    await update.message.reply_text(result)


# ---------- راهنما ----------

async def help_command(update: Update, context):

    await update.message.reply_text(
"""
/status
/economy
/military
/attack
/shop
"""
    )


# ---------- فروشگاه ----------

async def shop(update: Update, context):

    await update.message.reply_text(
"""
🛒 فروشگاه

به زودی:

🚀 موشک

🚜 تانک

✈️ هواپیما

🚢 ناو

🛡 پدافند
"""
    )


# ---------- اجرا ----------

def main():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("economy", economy))
    app.add_handler(CommandHandler("military", military))
    app.add_handler(CommandHandler("attack", attack))
    app.add_handler(CommandHandler("shop", shop))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot Started...")

    app.run_polling()


if __name__ == "__main__":
    main()
