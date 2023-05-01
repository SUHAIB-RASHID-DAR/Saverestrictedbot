from pyrogram import filters
from pyrogram.errors import FloodWait, InviteHashInvalid, InviteHashExpired, UserAlreadyParticipant
from datetime import datetime as dt
import os
import re
import subprocess
import time

from main.plugins.pyroplug import get_msg
from main.plugins.helpers import get_link, join

#Join private chat-------------------------------------------------------------------------------------------------------------
async def join(client, invite_link):
    try:
        await client.join_chat(invite_link)
        return "Successfully joined the Channel"
    except UserAlreadyParticipant:
        return "User is already a participant."
    except (InviteHashInvalid, InviteHashExpired):
        return "Could not join. Maybe your link is expired or Invalid."
    except FloodWait as e:
        return f"Too many requests, try again later after {e.x} seconds."
    except Exception as e:
        print(e)
        return "Could not join, try joining manually."

#Regex---------------------------------------------------------------------------------------------------------------
#to get the url from event
def get_link(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    try:
        link = [x[0] for x in url][0]
        if link:
            return link
        else:
            return False
    except Exception:
        return False

#Screenshot---------------------------------------------------------------------------------------------------------------
def hhmmss(seconds):
    x = time.strftime('%H:%M:%S', time.gmtime(seconds))
    return x

async def screenshot(video, duration, sender):
    if os.path.exists(f'{sender}.jpg'):
        return f'{sender}.jpg'
    time_stamp = hhmmss(int(duration) / 2)
    out = dt.now().isoformat("_", "seconds") + ".jpg"
    cmd = [
        "ffmpeg",
        "-ss",
        f"{time_stamp}",
        "-i",
        f"{video}",
        "-frames:v",
        "1",
        f"{out}",
        "-y"
    ]
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    x = stderr.decode().strip()
    y = stdout.decode().strip()
    if os.path.isfile(out):
        return out
    else:
        None

#Main Function------------------------------------------------------------------------------------------------------------
@Client.on_message(filters.private)
async def clone(client, message):
    if message.reply_to_message and message.reply_to_message.text == "Send me the message link you want to start saving from, as a reply to this message.":
        return
    try:
        link = get_link(message.text)
        if not link:
            return
    except TypeError:
        return
    try:
        join_message = await join(client, "FORCE_SUB_CHANNEL_USERNAME")
        if join_message != "Successfully joined the Channel":
            await message.reply(join_message)
            return
    except FloodWait as e:
       
