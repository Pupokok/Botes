from aiogram.fsm.state import StatesGroup, State


class Adm_send_fol(StatesGroup):
    first_mes = State()


class Adm_send_nofol(StatesGroup):
    send_nofol = State()