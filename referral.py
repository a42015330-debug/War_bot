# referral.py


from database import change_money


REFERRAL_REWARD = 500



def referral_link(user_id):

    return (
        f"https://t.me/atlarsanibot?start={user_id}"
    )



def give_reward(user_id):

    change_money(
        user_id,
        REFERRAL_REWARD
    )


    return f"""

🎁 دعوت موفق بود!

💰 جایزه شما:
{REFERRAL_REWARD} تومان

"""
