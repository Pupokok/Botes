import os

from dotenv import load_dotenv

from aiogram import Router, F, types
from aiogram.types import PreCheckoutQuery, SuccessfulPayment


from data_base.requests import set_time_subs

from keyboards.client_kb import kb_active_client_main

load_dotenv()
router = Router()


@router.message(F.text.in_("Купить подписку ✅"))
async def buy_subs(message: types.Message):
    await message.answer_invoice(
        title="Оформление подписки✅",
        description="Подписка на 30 дней",
        payload="month_sub",
        provider_token=os.getenv("YOOTOKEN"),
        currency="rub",
        start_parameter="pay_subscrip",
        prices=[{"label": "Руб", "amount": 50000}],
        provider_data=None,
        need_name=True,
        need_phone_number=False,
        need_email=True,
        need_shipping_address=False,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        reply_markup=None,
        request_timeout=30
    )    

@router.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    if pre_checkout_query.order_info:
        mes_id = pre_checkout_query.from_user.id
        await set_time_subs(mes_id)
        await pre_checkout_query.answer(ok=True)
        await pre_checkout_query.bot.send_message(chat_id=pre_checkout_query.from_user.id,
                                                  text="Вы успешно оплатили подписку на месяц",
                                                  reply_markup=kb_active_client_main)
        print(pre_checkout_query)
    else:
        await pre_checkout_query.answer(ok=False, error_message="Оплата не прошла успешно")
        print(pre_checkout_query)
