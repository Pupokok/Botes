from sqlalchemy import BigInteger, ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from os import getenv
from dotenv import load_dotenv

load_dotenv()
url = getenv("ENGINE")
engine = create_async_engine(url=url, echo=True)

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger, unique=True)
    referer_id = mapped_column(BigInteger)
    subscriptions: Mapped["Subscription"] = relationship(back_populates="user")
    vouchers: Mapped["Voucher"] = relationship(back_populates="user")

class Subscription(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(BigInteger, ForeignKey("users.tg_id", onupdate="CASCADE"))
    start_date = mapped_column(DateTime)
    end_date = mapped_column(DateTime)
    user: Mapped["User"] = relationship(back_populates="subscriptions")

class Voucher(Base):
    __tablename__ = "vouchers"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_tg_id = mapped_column(BigInteger, ForeignKey("users.tg_id", onupdate="CASCADE"))
    vaucher: Mapped[str] = mapped_column(String(255))
    user: Mapped["User"] = relationship(back_populates="vouchers")

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)