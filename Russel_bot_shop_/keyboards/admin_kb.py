from aiogram import types 

kb_admin = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text="Добавить товар"),
            types.KeyboardButton(text="Изменить товар"),
            types.KeyboardButton(text="Меню товара")
        ],
        [
            types.KeyboardButton(text="Поменять курс юаней")
        ]

    ], 
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)