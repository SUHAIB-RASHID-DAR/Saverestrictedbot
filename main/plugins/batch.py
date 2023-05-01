
# Github.com/SUHAIB-RASHID-DAR

"""
Plugin for both public & private channels!
"""

import time, os, asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from main.plugins.pyroplug import check, get_bulk_msg
from main.plugins.helpers import get_link, screenshot

from pyrogram.errors import FloodWait

from ethon.pyfunc import video_metadata
from ethon.telefunc import force_sub

ft = f"To use this bot you've to join @{fs}."

batch = []
batch_ = []

async def get_pvt_content(client, chat, id):
    msg = await client.get_messages(chat, ids=id)
    return msg

@Client.on_message(filters.private & filters.regex("^/batch"))
async def _batch(client, message):
    if message.from_user.id != AUTH:
        return
    # wtf is the use of fsub here if the command is meant for the owner? 
    # well am too lazy to clean 
    s, r = await force_sub(client, fs, message.from_user.id, ft) 
    if s == True:
        await message.reply(r)
        return       
    if f'{message.from_user.id}' in batch:
        return await message.reply("You've already started one batch, wait for it to complete you dumbfuck owner!")
    if s != True:
        msg = await message.reply("Send me the message link you want to start saving from.")
        link = await client.listen(msg)
        try:
            _link = get_link(link.text)
        except Exception:
            await message.reply("No link found.")
            return
    else:
        _link = ""
    msg = await message.reply("Send me the number of files/range you want to save from the given message.")
    _range = await client.listen(msg)
    try:
        value = int(_range.text)
        if value > 100:
            await message.reply("You can only get upto 100 files in a single batch.")
            return
    except ValueError:
        await message.reply("Range must be an integer!")
        return
    if s != True:
        await message.reply(r)
        return
    batch.append(f'{message.from_user.id}')
    batch_.append(f'{message.from_user.id}')
    cd = await message.reply("**Batch process ongoing.**\n\nProcess completed: ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("CANCEL❌", callback_data="cancel")]]))
    await run_batch(client, message.from_user.id, value, cd, _link) 
    await cd.delete()
    batch.clear()
    batch_.clear()
    
