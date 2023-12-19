from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    name = State()
    descr = State()
    price = State()
    photo = State()

class OrderFood(StatesGroup):
    choosing_food_name = State()


class Add_sneakers(StatesGroup):
    sneack_id = State()
    sneack_name = State()
    sneack_descr = State()
    sneack_price = State()
    sneack_photo = State()
    
class Currency(StatesGroup):
    currency_1 = State()