#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACHIYA LK | [____ACHIYA____]

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import pyrogram


from tobrot import (
    AUTH_CHANNEL
)


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        # leave chat
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    # await message.reply_text("No one is gonna help you! 🤣🤣🤣🤣", quote=True)
    #channel_id = str(AUTH_CHANNEL)[4:]
    #message_id = 99
    # display the /help
    
    await message.reply_text("""Join this group for help-- @atvreqs\n\n PLEASE READ THIS 👉 https://t.me/c/1338634999/55 \n\n © [ _ _ _ _ ACHIYA _ _ _ _ ] \n\n <b>COMMANDS</b>\n /gleech@achi - Torrent/URL to GDrive\n /tleech@achi - Telegram Files to GDrive\n /ytdl@achi - Youtube vids to GDrive""", disable_web_page_preview=True)


async def rename_message_f(client, message):
    inline_keyboard = []
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            text="[____ACHIYA____]"
        )
    ])
    reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text(
        "please use @renamebot",
        quote=True,
        reply_markup=reply_markup
    )
