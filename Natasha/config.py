import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_USERNAME = getenv("BOT_USERNAME", "MrsNatashaBot")
BOT_TOKEN = getenv("BOT_TOKEN", "5679131405:AAF2TOcQTtV6yqHpYoh998y8HYeEdZlOWoE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AQA5xTB1DlB6yA4y92zBqjro-YXMylufoB4wKR7LEsIHPFc4xlOfBJl15GuRb22lBiIQC3cGlUhynU3Wb8c3pXLfRXFOtjYPIPQZ4mZ92EfynyG4_arwCwC66nq9KR0r1w0SVaei0486JM6jGKxVcxp02mb9Kin_Qbyz4A5EymZ8EZifo2pvax7zSPO6l-Y8XFErj7Yu0g2eTX5vFJoJYg02O0buwsLWsnajEauE5tlgyDI0TvNfZSOZwuZm24CAJJEnyHE5h04PLuU0a4C50oZUBLJhVg9e3VUaDswmMq10aausd8nTcUMc-PrAuCe_lo3q77naudDG9XibN69satMnAAAAAWJg2aAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5616461719").split()))
aiohttpsession = aiohttp.ClientSession()
