from pyrogram import idle
from pyrogram import Client as Bot
from Nibbi.Modules.cache.clientbot import run
from Nibbi.config import API_ID, API_HASH, BOT_TOKEN

    
bot = Bot(
    ":Nibbi:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Nibbi/Plugins")
)

bot.start()
run()
idle()
