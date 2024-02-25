from aiogram.types import Message
from aiogram.enums import ChatAction
from aiogram import types, F, Router
from aiogram.utils.deep_linking import decode_payload
from aiogram.utils.chat_action import ChatActionSender
from aiogram.utils.deep_linking import create_start_link
from aiogram.filters import CommandStart, CommandObject, Command

from dotenv import load_dotenv

from data_base.requests import get_end_time, get_ref, get_time, get_vouchers, set_user

from inline_keyboards import first_inkb_bd, get_5K_inkb, support_inkb, mine_inkb

from keyboards.builders import rep_builder_video
from keyboards.client_kb import kb_client_main, kb_active_client_main

from pay.payment import buy_subs

from text.text_for_bot import Texts


load_dotenv()
router = Router()


@router.message(CommandStart())
async def start(message: Message, command: CommandObject):
    mes_id = message.from_user.id
    if command.args:
        try:
            referral_id = int(decode_payload(command.args))                             # Попытка декодировать и преобразовать referral_id к целому числу
            if referral_id == mes_id:
                await message.answer("Нельзя использовать свою реферальную ссылку!!!",      # Случай использования собственной реферальной ссылки
                                     reply_markup=kb_client_main)
            else:
                await message.answer(text=Texts.text_greeting,                    # Случай использования реферальной ссылки другого пользователя                   
                                     reply_markup=await first_inkb_bd())
                await set_user(mes_id, referral_id)
        except ValueError:
            await message.answer("Произошла ошибка при обработке реферальной ссылки.")
    else:
        await message.answer(text=Texts.text_greeting,                                # Случай запуска бота без использования реферальной ссылки
                             reply_markup=await first_inkb_bd())
        await set_user(mes_id)
        

@router.message(F.text == "Получить 5.000₽ 💸")
async def get_5k(message: Message):
    await message.answer(text=Texts.get_5k_text,
                         reply_markup=get_5K_inkb)


@router.message(F.text == "Забрать ваучер 🎟️")
async def vauch(message: Message):
    await message.answer(text=Texts.vauch_hand)

@router.message(F.text == "🎟️ Ваучер")
async def vauch_active(message: Message):
    vouchers = await get_vouchers()
    if not vouchers:
        await message.answer(text="К сожалению, пока нет активных ваучеров.")
    else:
        await message.answer(text=vouchers)
        # await message.answer(text=Texts.vauch_active)

@router.message(F.text == "Пригласить друга 🎁")
async def vauch(message: Message):
    await message.answer(text=Texts.vauch_hand)


@router.message(F.text == "Обучение 🕹️")
async def trening(message: Message):
    await message.answer(text="Просмотрите и узнайте основы",
                         reply_markup=await rep_builder_video())


@router.message((F.text == "Мотивация") | (F.text == "1 Урок"))
async def send_video(message: Message):
    sender = ChatActionSender(
        bot=message.bot,
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_VIDEO,)
    async with sender:
            if F.text == "Мотивация":
                await message.answer_video(video=types.FSInputFile(
                    "/home/feofan/Рабочий стол/rocket_queen/kwork/video/IMG_9013.MP4"))
            elif F.text == "1 Урок":
                await message.answer_video(video=types.FSInputFile(
                    "/home/feofan/Рабочий стол/rocket_queen/kwork/video/IMG_9014.MP4"))


@router.message(F.text == "Бесплатная стратегия 🆓")
async def strateg(message: Message):
    sender = ChatActionSender(
        bot=message.bot,
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_VIDEO,)
    async with sender:
        await message.answer_video(video=types.FSInputFile("/home/feofan/Рабочий стол/rocket_queen/kwork/video/IMG_9013.MP4"))


@router.message(F.text == "Мины 💣")
async def mines(message: Message):
    await message.answer(text=Texts.mines,
                         reply_markup=mine_inkb)


@router.message(F.text == "⚙️ Тех. поддержка")
async def supports(message: Message):
    await message.answer(text=Texts.support,
                         reply_markup=support_inkb)


@router.message(F.text == "Назад")
async def back(message: Message):
    await message.answer(text="Вы в главном меню",
                         reply_markup=kb_client_main)

@router.message(F.text == "🎁 Пригласить друга")
async def invite_friend(message: Message):
    mes_id = message.from_user.id
    ref = await get_ref(mes_id)
    link = await create_start_link(message.bot, payload=str(mes_id), encode=True)
    inv = Texts.invite(link, ref)
    await message.answer(text=inv)

@router.message(Command("main"))
async def main_keyb(message: Message):
    await message.answer(text="Вы в главном меню",
                               reply_markup=kb_client_main) 

@router.message(Command("active", prefix=("1!?")))
async def active_keyb(message: Message):
    times_end = await get_end_time(message.from_user.id)
    if times_end:
        await message.answer(text="Вы в главном меню активного пользователя",
                                   reply_markup=kb_active_client_main) 
    else:
        await message.answer(text="Ваша подписка не оплачена",
                                   reply_markup=kb_client_main) 
        await buy_subs(message)        
        

@router.message(F.text == "💼 Личный кабинет")
async def profile(message: Message, ):
    getting = await get_time(message.from_user.id)
    pers_inf = f"Активная подписка: {getting} дней" 
    await message.answer(text=pers_inf,
                         reply_markup=kb_active_client_main)


@router.message(F.text == "📚 Инструкция")
async def instructions(message: Message):
    await message.answer(text=Texts.instruc,
                         reply_markup=kb_active_client_main) 
