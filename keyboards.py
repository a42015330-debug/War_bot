# keyboards.py

from telegram import ReplyKeyboardMarkup



def main_menu():

    buttons = [

        ["🌍 کشور من", "👤 پروفایل"],

        ["⚔️ ارتش", "🏪 فروشگاه"],

        ["💰 اقتصاد", "🧠 ماموریت ریاضی"],

        ["🚀 حمله", "🤝 دیپلماسی"]

    ]

    return ReplyKeyboardMarkup(
        buttons,
        resize_keyboard=True
    )




def country_menu(countries):

    buttons=[]

    for c in countries:

        buttons.append([c])


    return ReplyKeyboardMarkup(
        buttons,
        resize_keyboard=True
    )




def shop_menu():

    buttons=[

        ["🪖 خرید سرباز"],

        ["🚀 خرید موشک"],

        ["🛩 خرید هواپیما"],

        ["🚢 خرید ناو"],

        ["🛡 خرید پدافند"],

        ["⬅️ بازگشت"]

    ]


    return ReplyKeyboardMarkup(
        buttons,
        resize_keyboard=True
    )





def math_menu():

    buttons=[

        ["آسان 🟢"],

        ["متوسط 🟡"],

        ["سخت 🔴"],

        ["خیلی سخت ⚫"]

    ]


    return ReplyKeyboardMarkup(
        buttons,
        resize_keyboard=True
    )
