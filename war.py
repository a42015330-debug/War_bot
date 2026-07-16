# war.py

import random

from database import change_money





def battle(
attacker,
defender
):


    attack_power = (

        attacker[7]
        +
        defender[8] * 0

    )


    defense_power = defender[12]



    if attack_power > defense_power:


        reward = int(
            defender[5] * 0.5
        )


        change_money(
            attacker[1],
            reward
        )


        return {

        "نتیجه":"پیروزی",

        "جایزه":reward

        }




    else:


        return {


        "نتیجه":"شکست",

        "جایزه":0

        }






def attack_message(result):


    if result["نتیجه"]=="پیروزی":


        return (

        "🎉 پیروزی در جنگ!\n\n"

        f"💰 غنیمت دریافت شده: "
        f"{result['جایزه']} تومان"

        )


    else:


        return (

        "❌ شکست خوردید!\n"

        "قدرت نظامی شما کافی نبود."

        )
