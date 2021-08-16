# SLT BrecLand <https://t.me/SLTBrecLand>
# @Damantha_Jasinghe

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from DTSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from DTSongBot import DTbot as app
from DTSongBot import LOGGER

pm_start_text = """
🌟**Heya** [{}](tg://user?id={}), **I'm** 🎧 **Song Download bot In Telegram You can download songs into me**👨‍💻  🎵
 Send A /help command in see my more commands and Help
🤖A bot by @omindas 🤖 ⚡ Powerd by @sdprojectupdates 💥💥
Updates channel @sdprojectupdates 
  My Source Code Is Comming Soon❤️❤️
"""

help_text = """
**Welcome to help room****My commands a bot by @omindas**
- /song <song name>: download songs via Youtube
- /saavn <song name>: download songs via JioSaavn
- /deezer <song name>: download songs via Deezer
-💎Send youtube url to my pm for download it on audio format
👨‍💻A bot by @omindas👨‍💻.........🤗
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="☀️Add Me Group", url="https://t.me/@SD_Song_bot?startgroup=true"
                    ),
                    InlineKeyboardButton(
                        text="🎈 Dev 🎈", url="https://t.me/omindas"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def start(client, message):
    await message.reply(help_text)

app.start()
LOGGER.info("DTSongBot is online.")
idle()
