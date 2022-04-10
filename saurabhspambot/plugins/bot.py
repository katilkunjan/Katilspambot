import os
import asyncio
import sys
import git
import heroku3
from saurabhspambot import saurabh, saurabh2, saurabh3, saurabh4, saurabh5 , saurabh6, saurabh7, saurabh8, saurabh9, saurabh10, saurabh11, saurabh12, saurabh13, saurabh14, saurabh15, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, saurabhversion
from saurabhspambot import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
from saurabhspambot import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

SAURABH_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/ba87c58f01a6fcb5ef512.jpg"
  

saurabh = "✯ KATILSPAM 𝗛𝗲𝗿𝗲 ✯\n\n"
saurabh += f"═══════════════════\n"
saurabh += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"
saurabh += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
saurabh += f"• **saurabhspambot ᴠᴇʀsɪᴏɴ**  : `{saurabhversion}`\n"
saurabh += f"═══════════════════\n\n"   

                                  
@saurabh.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@saurabh2.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@saurabh3.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@saurabh4.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@saurabh5.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@saurabh6.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@saurabh7.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@saurabh8.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@saurabh9.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@saurabh10.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@saurabh11.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@saurabh12.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@saurabh13.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@saurabh14.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@saurabh15.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
     await event.client.send_file(event.chat_id,
                                  SAURABH_PIC,
                                  caption=saurabh,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/heartbrokenperson1"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/FULL_MASTI_CLUBS")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/bhumiharsaurabh/saurabhspambot")
        ]
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@saurabh.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@saurabh2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@saurabh3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@saurabh4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@saurabh5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@saurabh6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@saurabh7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@saurabh8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@saurabh9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@saurabh10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@saurabh11.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@saurabh12.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@saurabh13.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@saurabh14.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@saurabh15.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀\n▒█▀▀▄ ▒█░░▒█ ░▒█░░\n▒█▄▄█ ▒█▄▄▄█ ░▒█░░\n\nϟ SAURABH SPAM BOT ϟ︎ `{ms}` ᴍs")
        
        

@saurabh.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@saurabh2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@saurabh3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@saurabh4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@saurabh5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@saurabh6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@saurabh7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@saurabh8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@saurabh9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@saurabh10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@saurabh11.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@saurabh12.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@saurabh13.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@saurabh14.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@saurabh15.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "**Restarting Your RiZoeL X Spam**.. Please Wait Until It Starts Again"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await saurabh.disconnect()
        except Exception:
            pass
        try:
            await saurabh2.disconnect()
        except Exception:
            pass
        try:
            await saurabh3.disconnect()
        except Exception:
            pass
        try:
            await saurabh4.disconnect()
        except Exception:
            pass
        try:
            await saurabh5.disconnect()
        except Exception:
            pass
        try:
            await saurabh6.disconnect()
        except Exception:
            pass
        try:
            await saurabh7.disconnect()
        except Exception:
            pass
        try:
            await saurabh8.disconnect()
        except Exception:
            pass
        try:
            await saurabh9.disconnect()
        except Exception:
            pass
        try:
            await saurabh10.disconnect()
        except Exception:
            pass
        try:
            await saurabh11.disconnect()
        except Exception:
            pass
        try:
            await saurabh12.disconnect()
        except Exception:
            pass
        try:
            await saurabh13.disconnect()
        except Exception:
            pass
        try:
            await saurabh14.disconnect()
        except Exception:
            pass  
        try:
            await saurabh15.disconnect()
        except Exception:
            pass  

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)

@saurabh.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply("Adding user as a sudo...")
        rizoel = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply to a user.")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added `{target}` ** as a sudo user 🔱 Restarting.. Please wait a minute...")
        heroku_var[saurabh] = newsudo   
   
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target
