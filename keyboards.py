from telegram import ReplyKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(
    [
        ["⚔ جنگ", "💰 اقتصاد"],
        ["🪖 ارتش", "🛒 فروشگاه"],
        ["🤝 اتحاد", "🏆 رتبه‌بندی"]
    ],
    resize_keyboard=True
)
