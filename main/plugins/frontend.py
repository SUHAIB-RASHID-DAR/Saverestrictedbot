# Github.com/SUHAIB-RASHID-DAR

import time
import os

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from main.plugins.pyroplug import get_msg
from main.plugins.helpers import get_link, join, screenshot
from ethon.telefunc import force_sub

#ft = f"To use this bot you've to join @{fs}."

message = "Send me the message link you want to start saving from, as a reply to this message."

process=[]
timer=[]
user=[]

# To-Do:
# Make these codes shorter and clean
# ofc will never do it.

@Client.on_message(filters.private)
async def clone(client: Client, message: Message):
    if message.reply_to_message and message.reply_to_message.text == message:
        return

    try:
        link = get_link(message.text)
        if not link:
            return
    except TypeError:
        return

    #s#, r = await force_sub(client, fs, message.from_user.id, ft)
    #if s:
        #await message.reply(r)
        #return

    edit = await message.reply("Processing!")
    if f'{message.from_user.id}' in user:
        return await edit.edit("Please don't spam links, wait until ongoing process is done.")

    user.append(f'{message.from_user.id}')
    try:
        if 't.me/+' in link:
            q = await join(userbot, link)
            await edit.edit(q)

        if 't.me/' in link:
            await get_msg(userbot, Bot, message.from_user.id, edit.message_id, link, 0)

    except FloodWait as fw:
        await client.send_message(message.from_user.id, f'Try again after {fw.x} seconds due to floodwait from telegram.')

    except Exception as e:
        print(e)
        await client.send_message(message.from_user.id, f"An error occurred during cloning of `{link}`\n\n**Error:** {str(e)}")

    ind = user.index(f'{message.from_user.id}')
    user.pop(int(ind))
