import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_USERNAME = getenv("BOT_USERNAME")
BOT_TOKEN = getenv("BOT_TOKEN")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5616461719").split()))
aiohttpsession = aiohttp.ClientSession()
