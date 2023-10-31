import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "27402720"))
	API_HASH = os.environ.get("API_HASH", "38f0682dce493e07863bc6783016e98d")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6416751021:AAGe6ate0K6ElNU4VYoMRSImUPw4xv5qF0E")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "BdFileStorageBot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001868162542"))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL', 'sharelinks.in')
	SHORTLINK_API = os.environ.get('SHORTLINK_API', '0e5f2972d232c6d9dbe4bfbd06654367866d1c1e')
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1150044195"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://theamanchaudhary:updatesbyaman@cluster0.rlgbj7c.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
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
├🔸 **Owner:** [King Sourab](https://t.me/KING_SOUROB) 
│
├🔹 **Bot Support:** [Support Group](https://t.me/KS_Korean_Drama_Hindi)
│
├🔸 **Bot Updates:** [Bots Channel](https://t.me/KS_Korean_Drama_Hindi)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [Aman Chaudhary](https://t.me/theamanchaudhary)
 
 I Am Super Noob Developer. Just Support My Hard Work.

"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is Premium **FileStore Bot**.

Send me any file I will give you a Permanent Sharable Link. 
And Your Files Auto Delete in 30 Minute

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from CopyRight Infringement Issue. I 

❌ PORNOGRAPHY CONTENTS are strictly prohibited & get Permanent Ban.
"""
