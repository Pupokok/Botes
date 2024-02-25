import re

from typing import Any

from contextlib import suppress

from datetime import datetime, timedelta

from aiogram import types, Router, F
from aiogram.types import ChatPermissions
from aiogram.filters import Command, CommandObject
from aiogram.exceptions import TelegramBadRequest

from text.text_for_bot import Texts



chan_r = Router()
chan_r.message.filter(F.chat.type == "supergroup", F.from_user.id == 1037988700)

def parse_time(time_string: str | None) -> datetime | None:
    if not time_string:
        return None
    
    match_ = re.match(r"(\d+)([a-z])", time_string.lower().strip())
    current_datetime = datetime.utcnow()

    if match_:
        value, unit = int(match_.group(1)), match_.group(2)

        match unit:
            
            case "s": time_delta = timedelta(seconds=value)
            case "h": time_delta = timedelta(days=value)
            case "d": time_delta = timedelta(hours=value)
            case "w": time_delta = timedelta(minutes=value)
            case _: return None
    else:
        return None
    
    new_datetime = current_datetime + time_delta
    return new_datetime
                

@chan_r.message(Command("ban"))
async def ban(message: types.Message, command: CommandObject) -> Any:
    reply = message.reply_to_message
    if not reply:
        return await message.answer("Нет ответа")
    until_date = parse_time(command.args)
    mention = reply.from_user.mention_html(reply.from_user.first_name)

    with suppress(TelegramBadRequest):
        await message.bot.ban_chat_member(
            chat_id=message.chat.id,
            user_id=reply.from_user.id,
            until_date=until_date
        )
        await message.answer(f"Забанен <b>{mention}</b>")

@chan_r.message(Command("mute"))
async def mute(message: types.Message, command: CommandObject) -> Any:
    replys = message.reply_to_message
    if not replys:
        return await message.answer("Нет ответа")
    until_date_mute = parse_time(command.args)
    mention_mute = replys.from_user.mention_html(replys.from_user.first_name)

    with suppress(TelegramBadRequest):
        await message.bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=replys.from_user.id,
            until_date=until_date_mute,
            permissions=ChatPermissions(can_send_messages=False)
        )
        await message.answer(f"Молчит <b>{mention_mute}</b>")
        await message.answer(text=Texts.bear_fook)
