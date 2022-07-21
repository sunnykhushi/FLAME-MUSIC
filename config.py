## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQABk6xKpg6I62pghWyrrwfkGZ7CPIoTZH02T0-bBZI6-d8L11G1i-G92T_y4Jixarjv7_E1nvDenRyHON644UDMxBNcpIskb8eztWq6rLWXcmAsI3GsrFXasTNRbbAC0H7c-ckgX8U1CysNB9dUAVoFNjXTA3HhDyefF-yqC2-e34aRkUhvlLuovAN_uRkW2BjybMvSXGffQShj1n62xjF_aBnANyRFY4WRZNDjUuvsSUM2wh2evXCU1v5d0avik-OAfbWgLuJO_3QGnZnYPA912w_BvxFvVrQsu09VFcaX7e4rotrrOA3eb6D_Fkgn1wD0jvf-tnNwVRKEDDVkY3YHe1RLJQA")
BOT_TOKEN = getenv("BOT_TOKEN", "5397534736:AAFdWBERiDvoLG85ix9c5_-tk4Bfr2KomSI")
BOT_NAME = getenv("BOT_NAME", "khushimusic_bot")
API_ID = int(getenv("API_ID", "13102178"))
API_HASH = getenv("API_HASH", "b6862f55a8927b55d3991bda2d2731e3")
OWNER_NAME = getenv("OWNER_NAME", "Sunny")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Sunnybabuu")
ALIVE_NAME = getenv("ALIVE_NAME", "Flame")
BOT_USERNAME = getenv("BOT_USERNAME", "sk_musicbbot")
OWNER_ID = getenv("OWNER_ID", "1902419660")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "khushi_assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "all_competitive_examm")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Flame_Updates")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1902419660").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/2c23f012984fa91267146.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/2c23f012984fa91267146.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/S780821/Flame-Music")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
