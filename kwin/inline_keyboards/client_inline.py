from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def first_inkb_bd():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Подробней об игре',
                                      callback_data='info_game_'))
    return keyboard.as_markup()

async def second_inkb_bd():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Получить сигнал 🚀',
                                      callback_data='get_signal_'))
    return keyboard.as_markup()

async def regist_inkb_bd():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text='Зарегистрироваться', callback_data='reg_url', url="https://1wyodo.top/"),
        InlineKeyboardButton(text='Я зарегистрировался', callback_data='i_regist')
    )
    return keyboard.adjust(1, 1).as_markup()


get_5K_inkb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Получить 5.000₽ 💸', callback_data='1win_url', url="https://1win.com")
        ]
    ]
)

support_inkb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Перейти к диалогу', callback_data='sup_dial', url="https://t.me/white_gora")
        ]
    ]
)

mine_inkb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Перейти на канал', callback_data='sup_dial', url="https://t.me/dabdobpe")
        ]
    ]
)

sub_channel_inkb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Подписаться', callback_data='sub_channel', url="https://t.me/dabdobpe")
        ]
    ]
)

