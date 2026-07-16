# main.py


from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)


from config import BOT_TOKEN

from keyboards import main_menu

from database import (
    get_player,
    create_player,
    name_exists
)


from countries import get_countries



async def start(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):


    user = update.effective_user


    player = get_player(
        user.id
    )


    if player:


        await update.message.reply_text(

        "🎖 شما قبلاً وارد بازی شده‌اید",

        reply_markup=main_menu()

        )

        return



    await update.message.reply_text(

    """

🌍 به بازی جنگ جهانی خوش آمدید!


ابتدا یک نام برای فرماندهی خود انتخاب کنید.


نام می‌تواند:
کشور خیالی،
حزب،
امپراتوری
یا اسم دلخواه شما باشد.


"""

    )


    context.user_data["register"]=True





async def message_handler(
update: Update,
context: ContextTypes.DEFAULT_TYPE
):


    text = update.message.text


    user = update.effective_user



    if context.user_data.get("register"):


        if name_exists(text):


            await update.message.reply_text(

            "❌ این نام قبلاً انتخاب شده است"

            )

            return



        context.user_data["name"]=text


        context.user_data["register"]=False


        await update.message.reply_text(

        "🌍 کشور خود را انتخاب کنید:",

        reply_markup=
        main_menu()

        )

        return




    await update.message.reply_text(

    "از منوی بازی استفاده کنید.",

    reply_markup=main_menu()

    )







def main():


    app = Application.builder().token(
        BOT_TOKEN
    ).build()



    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    app.add_handler(
        MessageHandler(
            filters.TEXT,
            message_handler
        )
    )



    print(
        "ربات فعال شد..."
    )


    app.run_polling()





if __name__=="__main__":

    main()
