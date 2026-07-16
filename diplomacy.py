# diplomacy.py



alliances=[]

peace=[]





def create_alliance(
country1,
country2
):


    alliances.append(
        (
        country1,
        country2
        )
    )


    return (

    "🤝 اتحاد ایجاد شد\n"

    f"{country1} و {country2}"

    )





def make_peace(
country1,
country2
):


    peace.append(
        (
        country1,
        country2
        )
    )


    return (

    "🕊 قرارداد صلح امضا شد\n"

    f"{country1} و {country2}"

    )





def show_alliances():


    if not alliances:

        return "❌ هنوز اتحادی وجود ندارد"



    text="🤝 اتحادها:\n\n"


    for a in alliances:

        text += (
            f"🌍 {a[0]} + {a[1]}\n"
        )


    return text
