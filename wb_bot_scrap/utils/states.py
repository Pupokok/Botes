from aiogram.fsm.state import StatesGroup, State


class Currency(StatesGroup):
    url = State()



class Times(StatesGroup):
    first_var = State()
    second_var = State()