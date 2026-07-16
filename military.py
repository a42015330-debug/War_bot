# military.py


WEAPONS={


"سرباز":
{
"قیمت":100,
"قدرت":1
},


"تانک":
{
"قیمت":5000,
"قدرت":20
},


"جنگنده":
{
"قیمت":100000,
"قدرت":100
},


"ناو":
{
"قیمت":100000,
"قدرت":150
},


"پدافند":
{
"قیمت":5000,
"قدرت":50
},


"موشک ساده":
{
"قیمت":500,
"قدرت":40
},


"موشک متوسط":
{
"قیمت":50000,
"قدرت":150
},


"موشک پیشرفته":
{
"قیمت":500000,
"قدرت":500
}


}





def get_price(item):

    return WEAPONS[item]["قیمت"]





def get_power(item):

    return WEAPONS[item]["قدرت"]





def calculate_attack(player):

    power=0


    # ستون‌های دیتابیس

    power += player[7] * 1

    power += player[8] * 20

    power += player[9] * 100

    power += player[10] * 150

    power += player[11] * 200


    return power





def calculate_defense(player):

    return player[12]
