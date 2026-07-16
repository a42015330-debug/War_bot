# shop.py

from military import WEAPONS
from database import change_money



def show_shop():

    text = "🏪 فروشگاه نظامی\n\n"


    for item,data in WEAPONS.items():

        text += (
            f"🔹 {item}\n"
            f"💰 قیمت: {data['قیمت']} تومان\n"
            f"⚔️ قدرت: {data['قدرت']}\n\n"
        )


    return text





def buy_item(
telegram_id,
item
):


    if item not in WEAPONS:

        return "❌ این وسیله وجود ندارد"



    price = WEAPONS[item]["قیمت"]


    player_money = 0


    # در main.py موجودی بررسی می‌شود


    return (
        f"✅ درخواست خرید {item} ثبت شد\n"
        f"💰 قیمت: {price} تومان"
    )
