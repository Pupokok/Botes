from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message

from inline_keyboards.client_inline import sub_channel_inkb

class CheckSubscription(BaseMiddleware):
    
    async def __call__(
        self, 
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    )-> Any:
        chat_member = await event.bot.get_chat_member(chat_id="@dabdobpe", user_id=event.from_user.id)

        if chat_member.status == "left":
            await event.answer('Подпишись на канал',
                               reply_markup=sub_channel_inkb)
        else:
            return await handler(event, data)
