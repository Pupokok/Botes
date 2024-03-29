from aiogram import types

kb_client = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = types.KeyboardButton(text='Каталог')
button_2 = types.KeyboardButton(text='Secret')
# button_3 = types.KeyboardButton(text='/Catalog')
# button_3 = types.KeyboardButton(text='/Admin')
kb_client.add(button_1, button_2)#, button_3)

main_inline_keyboard = types.InlineKeyboardMarkup(row_width=5)
main_inline_keyboard.add(
    types.InlineKeyboardButton(text='🚙 Auto', callback_data='open_main_inkb_car')
)
main_inline_keyboard.add(
    types.InlineKeyboardButton(text='🚲 Motorbike', callback_data='open_main_inkb_mot')
)

cars_submenu_inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
car_buttons = [
    types.InlineKeyboardButton(text='Lexus', callback_data='open_models_submenu_inkb_car_lexus'),
    types.InlineKeyboardButton(text='Audi', callback_data='open_models_submenu_inkb_car_audi'),
    types.InlineKeyboardButton(text='BMW', callback_data='open_models_submenu_inkb_car_bmw'),
    types.InlineKeyboardButton(text='Mercedes-Benz', callback_data='open_models_submenu_inkb_car_mers'),
    types.InlineKeyboardButton(text='⬅ Back ⬅', callback_data='Back_on_main_menu_car')
]
cars_submenu_inline_keyboard.row(*car_buttons)

cars_submenu_models_lexus_inline_keyboard = types.InlineKeyboardMarkup()
models_lexus_buttons = [
    types.InlineKeyboardButton(text='LX', callback_data='cars_submenu_models_lexus_inline_button:1'),
    types.InlineKeyboardButton(text='RX', callback_data='cars_submenu_models_lexus_inline_button:2'),
    types.InlineKeyboardButton(text='⬅ Back ⬅', callback_data='Back_on_main_menu_car_brand')
]
cars_submenu_models_lexus_inline_keyboard.row(*models_lexus_buttons)

cars_submenu_models_audi_inline_keyboard = types.InlineKeyboardMarkup()
models_audi_buttons = [
    types.InlineKeyboardButton(text='A6', callback_data='audi_a6'),
    types.InlineKeyboardButton(text='A7', callback_data='audi_a7'),
    types.InlineKeyboardButton(text='⬅ Back ⬅', callback_data='back_out')
]
cars_submenu_models_audi_inline_keyboard.row(*models_audi_buttons)

cars_submenu_models_bmw_inline_keyboard = types.InlineKeyboardMarkup()
models_bmw_buttons = [
    types.InlineKeyboardButton(text='X5(E53)', callback_data='cars_bmw_submenu_inkb:x5'),
    types.InlineKeyboardButton(text='X6M', callback_data='cars_bmw_submenu_inkb:x6m'),
    types.InlineKeyboardButton(text='⬅ Back ⬅', callback_data='back_out_on_bmw')
]
cars_submenu_models_bmw_inline_keyboard.row(*models_bmw_buttons)

cars_submenu_models_mers_inline_keyboard = types.InlineKeyboardMarkup()
models_mers_buttons = [
    types.InlineKeyboardButton(text='CLS(5.5)', callback_data='cars_mers_submenu_inkb:cls'),
    types.InlineKeyboardButton(text='W140', callback_data='cars_mers_submenu_inkb:w140'),
    types.InlineKeyboardButton(text='⬅ Back ⬅', callback_data='back_out_on_mers')
]
cars_submenu_models_mers_inline_keyboard.row(*models_mers_buttons)

mots_submenu_inline_keyboard = types.InlineKeyboardMarkup(row_width=5)
mot_buttons = [
    types.KeyboardButton(text='BMW', callback_data='mot_submenu_inline_button:1'),
    types.KeyboardButton(text='Kawasaki', callback_data='mot_submenu_inline_button:2'),
    types.KeyboardButton(text='⬅ Back ⬅', callback_data='Back_on_main_menu_mot')
]
mots_submenu_inline_keyboard.row(*mot_buttons)

# mots_submenu_inline_keyboard.add(types.InlineKeyboardButton(text='BMW', callback_data='mot_submenu_inline_button:1'),
#                                  types.InlineKeyboardButton(text='Kawasaki', callback_data='mot_submenu_inline_button:2')
#                                  )
                

# cars_submenu_inline_keyboard.add(types.InlineKeyboardButton(text='Lexus', callback_data='car_submenu_inline_button:1'))
# cars_submenu_inline_keyboard.add(types.InlineKeyboardButton(text='Audi', callback_data='car_submenu_inline_button:2'))

# cars_submenu_inline_keyboard.add(types.InlineKeyboardButton(text='Lexus', callback_data='car_submenu_inline_button:1'),
#                                  types.InlineKeyboardButton(text='⭕️⭕️⭕️⭕️ 𝐀𝐮𝐝𝐢', callback_data='car_submenu_inline_button:2') 
#                                 )   
# cars_submenu_inline_keyboard.insert(types.InlineKeyboardButton(text='Back', callback_data='car_submenu_inline_button:3'))

# mots_submenu_inline_keyboard.add(types.InlineKeyboardButton(text='BMW', callback_data='mot_submenu_inline_button:1'))
# mots_submenu_inline_keyboard.add(types.InlineKeyboardButton(text='Kawasaki', callback_data='mot_submenu_inline_button:2'))

















# inkb_client = InlineKeyboardMarkup(row_width=2)
# inkb_client.add(InlineKeyboardButton(text='Lexus LX 570 III Рестайлинг 2', url='https://auto.ru/cars/used/sale/lexus/lx/1120425649-7efe42cd/'),
#                 InlineKeyboardButton(text='Lexus GX 460 II Рестайлинг 2', url='https://auto.ru/cars/used/sale/lexus/gx/1120386994-0ce8a5c7/'),
#                 InlineKeyboardButton(text='Lexus LX 570 III Рестайлинг 2', url='https://auto.ru/cars/used/sale/lexus/lx/1120062461-e7fadda2/'),
#                 InlineKeyboardButton(text="Ref", callback_data='Ref')
#                 )



# cb = Callback_data()
# inkb_b1 = InlineKeyboardButton('Lexus', url='https://auto.ru/kazan/cars/lexus/all/')
# inkb_b2 = InlineKeyboardButton('Lexus LX 570 III Рестайлинг 2', url='https://auto.ru/cars/used/sale/lexus/lx/1120425649-7efe42cd/')
# inkb_b3 = InlineKeyboardButton('Lexus GX 460 II Рестайлинг 2', url='https://auto.ru/cars/used/sale/lexus/gx/1120386994-0ce8a5c7/')
# inkb_b4 = InlineKeyboardButton('Lexus LX 570 III Рестайлинг 2', url='https://auto.ru/cars/used/sale/lexus/lx/1120062461-e7fadda2/')
# inkb_b5 = InlineKeyboardButton(text='Refresh')
# inkb_client.insert(inkb_b1).insert(inkb_b2).insert(inkb_b3).add(inkb_b4)#.insert(inkb_b5)
# inkb_client.insert(inkb_b5)