from aiogram import types


main_admin_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_admin_kb.add(types.KeyboardButton(text='Add_product'),
                  types.KeyboardButton(text='/Delete product'),
                  types.KeyboardButton(text='Cancel'))
