from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards.admin_kb import kb_admin_send, kb_admin_panel, kb_adm_back

from utils.states import Adm_send_fol, Adm_send_nofol

router = Router()
is_admin = F.from_user.id.in_({121279882})

@router.message(Command("mod", prefix="1"), is_admin)
async def admin_panel(message: Message):
    await message.answer(text='Вы в меню модератора', reply_markup=kb_admin_panel)

@router.message(F.text == ("📝Отправить сообщение"), is_admin)
async def admin_send_mes(message: Message):
    await message.answer(text='Кому хотите отправить', reply_markup=kb_admin_send)
    

@router.message(F.text == ("подписчикам"), is_admin)
async def admin_send_folowers(message: Message, state: FSMContext):
    await state.set_state(Adm_send_fol.first_mes)
    await message.answer(text='Что хотите отправить', reply_markup=kb_adm_back)

@router.message(Adm_send_fol.first_mes, is_admin)
async def handle_send_follow(message: Message, state: FSMContext):
    await message.send_copy(chat_id=121279882, reply_markup=kb_admin_panel)
    await state.clear()


@router.message(F.text == ("не подписчикам"), is_admin)
async def admin_send_no_folowers(message: Message, state: FSMContext):
    await state.set_state(Adm_send_nofol.send_nofol)
    await message.answer(text='Что хотите отправить', reply_markup=kb_adm_back)

@router.message(Adm_send_nofol.send_nofol, is_admin)
async def handle_send_nofolow(message: Message, state: FSMContext):
    await message.send_copy(chat_id=656532358, reply_markup=kb_admin_panel)
    await state.clear()

