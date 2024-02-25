from aiogram import types 


kb_admin_send = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text="подписчикам"),
            types.KeyboardButton(text="не подписчикам"),
        ]
    ], 
    resize_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)

kb_adm_back = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text="Назад")
        ]

    ], 
    resize_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
    
)


kb_admin_panel = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text="🚀Ставим")
        ],

        [
            types.KeyboardButton(text="✅Успех"),
            types.KeyboardButton(text="♻️Возврат ставки")
        ],

        [
            types.KeyboardButton(text="❌Промах")
        ],

        [
            types.KeyboardButton(text="📝Отправить сообщение")
        ]
    ], 
    resize_keyboard=True,
    # one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)