from data_base.models import async_session
from data_base.models import User, Subscription, Voucher

from datetime import datetime, timedelta

from sqlalchemy import select, update, delete, func


# ваучеры закончить

async def get_vouchers():
    async with async_session() as session:
        vouches = await session.scalar(select(Voucher))
        return vouches


async def get_ref(tg_id):
    async with async_session() as session:
        referral = await session.scalar(select(func.count()).where(User.referer_id == tg_id))
        return referral


async def get_time(user_id):
    async with async_session() as session:
        times_subs = await session.scalar(select(Subscription).where(Subscription.user_id == user_id))
        start_date_user_subs = times_subs.start_date
        end_date_user_subs = times_subs.end_date
        quantity = (end_date_user_subs - start_date_user_subs).days
        return quantity

async def get_end_time(user_id):
    async with async_session() as session:
        time_now = datetime.now()
        times_subs = await session.scalar(select(Subscription).where(Subscription.user_id == user_id))
        
        if times_subs is None:
            return False
        
        end_date_user_subs = times_subs.end_date
        if time_now >= end_date_user_subs:
            return False
        else:
            return True



async def set_user(tg_id, referer_id=None):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        
        if not user:
            if referer_id != None:
                new_user = User(tg_id=tg_id,
                                referer_id=referer_id)
            else:
                new_user = User(tg_id=tg_id)
            session.add(new_user)
            await session.commit()


async def set_time_subs(user_id):
    async with async_session() as session:
        user_sub = await session.scalar(select(Subscription).where(Subscription.user_id == user_id))
        if not user_sub:
            time_now = datetime.now()
            end_date = time_now + timedelta(days=30)
            subscription = Subscription(user_id=user_id,
                                        start_date=time_now,
                                        end_date=end_date)
            session.add(subscription)
            await session.commit()
        else:
            current_time = datetime.now()
            if current_time <= user_sub.end_date:
                end_date_plus = user_sub.end_date + timedelta(days=30)
                user_sub.end_date = end_date_plus
                session.add(user_sub)
                await session.commit()
            else:
                start_date = current_time
                end_date = current_time + timedelta(days=30)
                user_sub.start_date = start_date
                user_sub.end_date = end_date
                session.add(user_sub)
                await session.commit()