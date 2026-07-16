# economy.py

import random



LEVELS = {


"آسان 🟢":
{
"جایزه":100,
"حد":50
},


"متوسط 🟡":
{
"جایزه":150,
"حد":200
},


"سخت 🔴":
{
"جایزه":200,
"حد":500
},


"خیلی سخت ⚫":
{
"جایزه":250,
"حد":1000
}

}




def create_math(level):


    data = LEVELS[level]


    a=random.randint(
        1,
        data["حد"]
    )


    b=random.randint(
        1,
        data["حد"]
    )


    operation=random.choice(
        ["+","-"]
    )


    if operation=="+":
        answer=a+b

    else:
        answer=a-b



    question=f"{a} {operation} {b} = ؟"


    return question,answer,data["جایزه"]





def country_income():

    return random.randint(
        50,
        300
    )
