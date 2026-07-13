import os
import random
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

TOKEN = os.getenv("8875469079:AAFjXwWvNr546xy0OArV6XO2OGaT2WlQIh8")

players = {}

countries = {
    "ایران": {"army":1000,"air":100,"navy":50,"money":5000},
    "آمریکا": {"army":3000,"air":500,"navy":400,"money":10000},
    "روسیه": {"army":2500,"air":400,"navy":300,"money":9000},
    "چین": {"army":2800,"air":450,"navy":350,"money":9500},
    "آلمان": {"army":2000,"air":300,"navy":150,"money":7000},
    "انگلیس": {"army":1800,"air":350,"navy":400,"money":8000}
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.id

    await update.message.reply_text(
        "🌍 به بازی جنگ جهانی خوش آمدید\n\n"
        "دستورات:\n"
        "/country - انتخاب کشور\n"
        "/status - وضعیت کشور\n"
        "/attack - حمله\n"
        "/peace - درخواست صلح\n"
        "/ally - اتحاد"
    )


async def country(update: Update, context):
    user = update.effective_user.id

    players[user] = {
        "country": random.choice(list(countries.keys())),
        "army":1000,
        "money":5000,
        "wins":0
    }

    await update.message.reply_text(
        f"🏳️ کشور شما انتخاب شد:\n"
        f"{players[user]['country']}\n\n"
        "آماده جنگ هستید!"
    )


async def status(update: Update, context):
    user = update.effective_user.id

    if user not in players:
        await update.message.reply_text("اول کشور انتخاب کن")
        return

    p = players[user]

    await update.message.reply_text(
        f"🌍 کشور: {p['country']}\n"
        f"⚔️ ارتش: {p['army']}\n"
        f"💰 پول: {p['money']}\n"
        f"🏆 پیروزی: {p['wins']}"
    )


async def attack(update: Update, context):
    user = update.effective_user.id

    if user not in players:
        await update.message.reply_text("اول کشور انتخاب کن")
        return

    enemy = random.choice(list(countries.keys()))

    power = random.randint(1,100)

    if power > 50:
        players[user]["wins"] += 1
        players[user]["money"] += 1000
        result = "✅ پیروز شدید"
    else:
        players[user]["army"] -= 200
        result = "❌ شکست خوردید"

    await update.message.reply_text(
        f"⚔️ جنگ با {enemy}\n\n{result}"
    )


async def peace(update: Update, context):
    await update.message.reply_text(
        "🕊️ پیمان صلح ثبت شد"
    )


async def ally(update: Update, context):
    await update.message.reply_text(
        "🤝 اتحاد نظامی تشکیل شد"
    )


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start",start))
    app.add_handler(CommandHandler("country",country))
    app.add_handler(CommandHandler("status",status))
    app.add_handler(CommandHandler("attack",attack))
    app.add_handler(CommandHandler("peace",peace))
    app.add_handler(CommandHandler("ally",ally))

    app.run_polling()


if name == "main":
    main()
