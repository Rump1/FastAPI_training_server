from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey


engine = create_async_engine("sqlite+aiosqlite:///data.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)

intpk = Annotated[int, mapped_column(primary_key=True)]


class Model(DeclarativeBase):
    pass


class UsersTable(Model):
    __tablename__ = "Users"

    id: Mapped[intpk]
    login: Mapped[str]
    password: Mapped[str]


class PersonalAccountTable(Model):
    __tablename__ = "PersonalAccount"

    id: Mapped[int] = mapped_column(ForeignKey("Users.id", ondelete="CASCADE"), primary_key=True)
    balance: Mapped[float]
    phone_number: Mapped[str]
    INN: Mapped[str]
    address: Mapped[str]


class CallsTable(Model):
    __tablename__ = "Calls"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("Users.id", ondelete="CASCADE"))
    duration: Mapped[int]
    cost: Mapped[float]
    city_id: Mapped[str] = mapped_column(ForeignKey("Cities.id", ondelete="CASCADE"))


class CitiesTable(Model):
    __tablename__ = "Cities"

    id: Mapped[intpk]
    city: Mapped[str]
    daily_rate: Mapped[float]
    night_rate: Mapped[float]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
