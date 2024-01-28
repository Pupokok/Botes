from aiogram import types 

kb_admin = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text="Добавить товар"),
            types.KeyboardButton(text="Сменить время")

        ]

    ], 
    resize_keyboard=True,
    selective=True
)