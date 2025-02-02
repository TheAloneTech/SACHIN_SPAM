import asyncio
import random
from telethon import events
from config import SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from nexichat.data import RAID, REPLYRAID, ALTRON, MRAID, SRAID, CRAID, ALTRON
from pyrogram import filters, Client

que = {}


@Client.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗥𝗮𝗶𝗱\n  » {hl}raid <count> <Username of User>\n  » {hl}raid <count> <reply to a User>"
    if e.sender_id in SUDO_USERS:
        mkraid = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)

        if len(mkraid) == 2:
            message = str(mkraid[1])
            a = await e.client.get_entity(message)
            g = a.id
            if int(g) in ALTRON:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ  sʜɪᴠᴀɴsʜ ᴘᴀᴘᴀ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(g) in SUDO_USERS:
                await e.reply("» ᴀʙᴇ.. ʏᴇ sᴜᴅᴏ ʟᴇᴋᴀʀ ʙᴀɪᴛʜᴀ ʜᴀɪ", parse_mode=None, link_preview=None)
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(mkraid[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                   caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in ALTRON:
                await e.reply("» ᴀʀᴇ.. ʏᴇ ᴛᴏ ᴛᴇʀᴀ  sʜɪᴠᴀɴsʜ ᴘᴀᴘᴀ ʜᴀɪ", parse_mode=None, link_preview=None)
            elif int(g) in SUDO_USERS:
                await e.reply("» ᴀʙᴇ.. ʏᴇ sᴜᴅᴏ ʟᴇᴋᴀʀ ʙᴀɪᴛʜᴀ ʜᴀɪ", parse_mode=None, link_preview=None)
            else:
                c = b.first_name
                counter = int(mkraid[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@                reply = random.choice(MRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.1)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(mkmr[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(MRAID)
                caption = f"{username} {reply}"
                await e.client.send_message(e.chat_id, caption)
                await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
