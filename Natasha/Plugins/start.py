import asyncio
import random
from time import time
from datetime import datetime
from Natasha.config import BOT_USERNAME
from Natasha.Modules.helpers.filters import command
from Natasha.Modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton




START_IMG = (
"https://te.legra.ph/file/24e09283605dd7e6160a1.jpg",
"https://te.legra.ph/file/2ea6a63d1738eec406e23.jpg",
"https://te.legra.ph/file/c6dc0b91fd56d5c99871b.jpg",
"https://te.legra.ph/file/fe68bd3a59c3ea6cbaac0.jpg",
"https://te.legra.ph/file/3f507b64e8a75b11f93b7.jpg",
"https://te.legra.ph/file/894061404d8e5d83a303c.jpg",
"https://te.legra.ph/file/17490b7b7600f2ac232b4.jpg",
"https://te.legra.ph/file/b23c22fea8b1718280856.jpg",
"https://te.legra.ph/file/61cad7f5ac55d77a951df.jpg",
"https://te.legra.ph/file/138690876272a96585f49.jpg",
"https://te.legra.ph/file/c73b942a4bc30aa56e729.jpg",
"https://te.legra.ph/file/21eb5abf4888394019c9c.jpg"
"https://te.legra.ph/file/e7d5d55910092de2b56df.jpg",
"https://te.legra.ph/file/95e864dfe3a410ccf20fa.jpg",

)



START_TEXT = """
ʜɪ ɢᴜʏꜱ,ɪ ᴀᴍ ɴᴀᴛᴀsʜᴀ 🇮🇳
⦿ ɪ'ᴍ ᴀ ꜱɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜꜱɪᴄ ʙᴏᴛ.
⦿ ɪ'ᴍ ᴠᴇʀʏ ғᴀꜱᴛ ᴀɴᴅ ᴍᴏʀᴇ ᴇꜰꜰɪᴄɪᴇɴᴛ. 
⦿ ɪ'ᴍ ᴘʀᴏᴠɪᴅᴇ ᴀᴡᴇꜱᴏᴍᴇ ꜱᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ.
⦿ɪ'ᴍ ғᴜʟʟʏ sᴛᴀʙʟᴇ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴀɴᴅ ᴢᴇʀᴏ ʟᴀɢs ᴀɴᴅ ᴅᴏᴡɴᴛɪᴍᴇ ɪssᴜᴇs.
⦿ ɪ ʜᴀᴠᴇ ᴀʟᴍᴏꜱᴛ ᴀʟʟ ꜰᴇᴀᴛᴜʀᴇꜱ ᴡʜɪᴄʜ ɴᴇᴇᴅꜱ ᴀ ᴍᴜꜱɪᴄ ʙᴏᴛ

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ꜰᴇᴀᴛᴜʀᴇꜱ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴄᴍᴅ ʙᴜᴛᴛᴏɴ ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱɪɴɢ ᴍᴇ.
"""






START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        random.choice(START_IMG),
        caption=(START_TEXT),
    reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        
        [
            InlineKeyboardButton("🧰 ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_cmd"),
            InlineKeyboardButton("🎓 ᴍᴀɪɴᴛᴀɪɴᴇʀ", url=f"https://t.me/Simple_Munda"),
        ]
   
     ]
  ),
)
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        random.choice(START_IMG),
        caption=(START_TEXT),
        reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        
        [
            InlineKeyboardButton("🧰 ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_cmd"),
            InlineKeyboardButton("🎓 ᴍᴀɪɴᴛᴀɪɴᴇʀ", url=f"https://t.me/Simple_Munda")
        ]
   
     ]
  ),
)



