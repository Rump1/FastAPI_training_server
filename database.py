from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


engine = create_async_engine("sqlite+aiosqlite:///data.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)

intpk = Annotated[int, mapped_column(primary_key=True)]


class Model(DeclarativeBase):
    pass


class ProvidersTable(Model):
    __tablename__ = "Providers"

    id: Mapped[intpk]
    login: Mapped[str]
    password: Mapped[str]

    clients: Mapped[list["ClientsTable"]] = relationship()


class ClientsTable(Model):
    __tablename__ = "Clients"

    id: Mapped[intpk]
    provider_id = mapped_column(ForeignKey("Providers.id", ondelete="CASCADE"))
    balance: Mapped[float]
    phone_number: Mapped[str]
    INN: Mapped[str]
    address: Mapped[str]

    provider: Mapped["ProvidersTable"] = relationship()
    calls: Mapped[list["CallsTable"]] = relationship()


class CallsTable(Model):
    __tablename__ = "Calls"

    id: Mapped[intpk]
    provider_id: Mapped[int] = mapped_column(ForeignKey("Providers.id", ondelete="CASCADE"))
    city_id: Mapped[str] = mapped_column(ForeignKey("Cities.id", ondelete="CASCADE"))
    duration: Mapped[int]
    cost: Mapped[float]

    client: Mapped["CitiesTable"] = relationship()
    city: Mapped["CitiesTable"] = relationship()


class CitiesTable(Model):
    __tablename__ = "Cities"

    id: Mapped[intpk]
    city: Mapped[str]
    daily_rate: Mapped[float]
    night_rate: Mapped[float]

    calls: Mapped[list["CallsTable"]] = relationship()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
