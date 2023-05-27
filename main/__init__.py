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
BOT_TOKEN = "6017979742:AAE_O4DFlKSaJm4FMt2RNwEkuTjjUwbd4Rw" 
SESSION = "BQCRDmS9q2Gyo1Y-DZ9dikRBmz8h3sMz6qJ_t8X7M3rQUQHuTHpToUQisvaBLONVr-NBkDXy42bVKMH-1bCi7y0ouyDe7OPfs62cw6Y9OeZF8yGuSNAV1HFDJUOOACAl9U9YohuKaLDwTQf9bRAowwR1FeibZhvFrdAI3maCth--2ljnqzSmnGZ55jKs8BrgPVhpJB-9uVMv3Kbriifck103TwEmArwp3arK5WElSb_WukT_Vm9okUmOym2hCfkMm2Nif_psu1sqdxKca_HTmzZDf4A7drQiJmAJlmoj8RCVYe1zHcR0-jj4iW2EcQ6JPUkTKYLBtJoS4ZdInCgS1dNeAAAAAW3tcvEA"
AUTH = 6139245297

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
