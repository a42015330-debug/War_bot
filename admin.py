# admin.py


ADMIN_USERNAME = "Amirrehi1"


CHANNEL_LINK = "https://t.me/atlarsanibot"



def is_admin(username):

    if username is None:
        return False


    username = username.replace("@","")


    return username == ADMIN_USERNAME





def admin_panel():

    return f"""

👑 پنل مدیریت


مدیر:
@{ADMIN_USERNAME}


📢 کانال رسمی:

{CHANNEL_LINK}



دستورات:

/users
تعداد کاربران


/status
وضعیت ربات


/give
دادن پول


"""
