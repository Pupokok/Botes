from aiogram import Router, F
from aiogram.types import CallbackQuery

from inline_keyboards.client_inline import regist_inkb_bd, second_inkb_bd

from keyboards.client_kb import kb_client_main

from text.text_for_bot import Texts


router = Router()
user_clicks = {}


@router.callback_query(F.data.startswith("info_game_"))
async def inf(query: CallbackQuery):
    await query.message.edit_text(text=Texts.second_text,
                                  reply_markup=await second_inkb_bd())
    await query.answer()

@router.callback_query(F.data == "get_signal_")
async def signal(query: CallbackQuery):
    await query.message.edit_text(text=Texts.third_text,
                                  reply_markup=await regist_inkb_bd())
    await query.answer()


@router.callback_query(F.data == "i_regist")
async def regist(query: CallbackQuery):
    user_id = query.from_user.id
    user_clicks[user_id] = user_clicks.get(user_id, 0) + 1
    if user_clicks[user_id] == 2:
        await query.message.answer(text="Вы в главном меню",
                                   reply_markup=kb_client_main)
        user_clicks.clear()

    elif user_clicks[user_id] < 2:
        await query.bot.send_message(user_id,
                                     text="«Сначала зарегистрируйте новый аккаунт и укажите промокод: Robot100»")
    await query.answer()
