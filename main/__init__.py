#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 9583161
API_HASH = "aecf9e2b7c655c4f916564ab6d598a73" 
BOT_TOKEN = "6283547148:AAFQDyUEzjCnf4QXBPdwfQUJzlrAxE_h5_U" 
SESSION = "BAAxhOmoByZg70r6JO-lB_0rudN-5s0LgiwU4mYr0XRcaNwU9yOMbx74Z_0AxjT-RoiT1fSYO_Mi3RkHa6Cq5fD6mIB6YNtWEzSNbLFl5qMRgZgp9wK4k7adaFJ8c3H_UFQp3qEAzEN3WpbMampzpT68KdC16jh9okhNT0kh4PaU0SkZeVtQkefSoAYhKs7gT0ozvapSjJ1lSsuD6tZage0Hs8PBNnirGX62yY191K6mhs0PVIwz49B0T37l8Ay-ojJUXTw7XV0KXgyFmqE0d0cZOoYy4iOY-8j8agJ8ilr8RfMQHyaWKl-7nI27OQadCLR3_kmqfOfqTapCt4916ZjHAAAAAWQMrCAA"
AUTH = 5973519392

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
