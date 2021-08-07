# SLT BrecLand <https://t.me/SLTBrecLand>
# @Damantha_Jasinghe

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from DTSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from DTSongBot import DTbot as app
from DTSongBot import LOGGER

pm_start_text = """
👋Heya👋 [{}](tg://user?id={}), 🤖I'm 🎧 Telegram Fast Song Download bot 🎵🌟
✳️✳️send a 👉 /help 👈 command for see a my commands✓😋
𝙰 𝙱𝚢 @omindas
𝚄𝚙𝚍𝚊𝚝𝚎 𝙲𝚑𝚊𝚗𝚗𝚊𝚕 @sdprojectupdates
"""

help_text = """
𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕋𝕠 ℍ𝕖𝕝𝕡 ℝ𝕠𝕠𝕞👇 𝕤𝕖𝕖 𝕒 𝕞𝕪 𝕔𝕠𝕞𝕞𝕒𝕟𝕕𝕤👇👇
- /song <song name>: download songs via Youtube
- /saavn <song name>: download songs via JioSaavn
- /deezer <song name>: download songs via Deezer
- Send youtube url to my pm for download it on audio format
A bot by @omindas and powerd by @sdprojectupdates
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
                        text="✳️𝑈𝑝𝑑𝑎𝑡𝑒 𝐶𝒉𝑎𝑛𝑛𝑎𝑙✳️", url="https://t.me/sdprojectupdates"
                    ),
                    InlineKeyboardButton(
                        text="🔥💥𝐷𝑒𝑣𝑒𝑙𝑜𝑝𝑒𝑟💥🔥", url="https://t.me/omindas"
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
LOGGER.info("sdSongBot is online.")
idle()
