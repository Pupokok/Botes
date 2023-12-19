from aiogram import types 

kb_client = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text="Актуальный курс"),
            types.KeyboardButton(text="Сроки доставки")
        ],
        [
            types.KeyboardButton(text="Итоговая стоимость")

        ],
        [
            types.KeyboardButton(text="Товар")
        ],
        [
            types.KeyboardButton(text="Оформить заказ")
        ]

    ], 
    resize_keyboard=True,
    # one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)
