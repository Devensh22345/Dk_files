import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "27402720"))
	API_HASH = os.environ.get("API_HASH", "38f0682dce493e07863bc6783016e98d")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6340952541:AAHgcJHFbwxs7YChge9gct8X5obgNqmYd8c")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "KS_Private_File_Robot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001887512620"))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL', 'sharelinks.in')
	SHORTLINK_API = os.environ.get('SHORTLINK_API', '0e5f2972d232c6d9dbe4bfbd06654367866d1c1e')
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1150044195 5674333293"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://theamanchaudhary:updatesbyaman@cluster0.rlgbj7c.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001967804966")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001716327321")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Heroku](https://heroku.com)
│
├🔸 **Owner:** [Sasuke](https://t.me/KING_SOUROB) 
│
├🔹 **Bot Support:** [Support Group](https://t.me/KS_Team_Live)
│
├🔸 **Bot Updates:** [Bots Channel](https://t.me/KS_Team_Live)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [Aman Chaudhary](https://t.me/theamanchaudhary)
 
 I Am Super Noob Developer. Just Support My Hard Work.

"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
