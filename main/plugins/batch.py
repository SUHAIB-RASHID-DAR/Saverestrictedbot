
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
#from ethon.telefunc import force_sub

#ft = f"To use this bot you've to join @{fs}."

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
    #s, r = await force_sub(client, fs, message.from_user.id, ft) 
    #if s == True:
        #await message.reply(r)
        #return       
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
    
@Client.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    batch_.clear()

async def run_batch(userbot, client, sender, range_, countdown, link):
    for i in range(range_ + 1):
        timer = 60
        if i < 25:
            timer = 5
        if i < 50 and i > 25:
            timer = 10
        if i < 100 and i > 50:
            timer = 15
        if not 't.me/c/' in link:
            if i < 25:
                timer = 2
            else:
                timer = 3
        try:
            check_ = batch_[0]
            count_down = f"**Batch process ongoing.**\n\nProcess completed: {i+1}"
            out = await get_bulk_msg(userbot, client, sender, link, i)
            if out is not None:
                if out - 5 > 300:
                    await client.send_message(sender, f'You have floodwaits of {out - 5} seconds, cancelling batch')
                    batch_.clear()
                    break
                else:
                    fw_alert = await client.send_message(sender, f'Sleeping for {out} second(s) due to telegram flooodwait.')
                    await asyncio.sleep(out)
                    await fw_alert.delete()
                    await get_bulk_msg(userbot, client, sender, link, i)
            protection = await client.send_message(sender, f"Sleeping for `{timer}` seconds to avoid Floodwaits and Protect account!")
            await countdown.edit(count_down)
            await asyncio.sleep(timer)
            await protection.delete()
        except IndexError:
            await client.send_message(sender, "Batch successfully completed!")
            await countdown.delete()
            break
        except Exception as e:
            print(e)
            if countdown.text != count_down:
                await countdown.edit(count_down)
