from aiogram import types 

kb_client_main = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text="Купить подписку ✅"),
        ],
        [
            types.KeyboardButton(text="🎁 Пригласить друга"),
            types.KeyboardButton(text="Обучение 🕹️")
        ],
        [
            types.KeyboardButton(text="Получить 5.000₽ 💸"),
            types.KeyboardButton(text="Забрать ваучер 🎟️")
        ],
        [
            types.KeyboardButton(text="Бесплатная стратегия 🆓"),
            types.KeyboardButton(text="Мины 💣")
        ],
        [
            types.KeyboardButton(text="⚙️ Тех. поддержка")
        ]
    ], 
    resize_keyboard=True,
    input_field_placeholder="Выберите действие из меню"
)

kb_active_client_main = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text="🎁 Пригласить друга"),
            types.KeyboardButton(text="📚 Инструкция")

        ],
        [
            types.KeyboardButton(text="💼 Личный кабинет"),
            types.KeyboardButton(text="⚙️ Тех. поддержка")
        ],
        [
            types.KeyboardButton(text="🎟️ Ваучер"),
            types.KeyboardButton(text="Мины 💣")
        ]
    
    ], 
    resize_keyboard=True,
    input_field_placeholder="Выберите действие из меню"
)

    
kb_back = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text="Назад")
        ]

    ], 
    resize_keyboard=True,
    input_field_placeholder="Выберите действие из меню"    
)

