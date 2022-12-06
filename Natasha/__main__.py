from pyrogram import idle
from pyrogram import Client as Bot
from Natasha.Modules.cache.clientbot import run
from Natasha.config import API_ID, API_HASH, BOT_TOKEN

    
bot = Bot(
    ":Natasha:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Natasha/Plugins")
)

bot.start()
run()
idle()
