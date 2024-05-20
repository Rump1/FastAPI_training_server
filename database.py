from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


engine = create_async_engine("sqlite+aiosqlite:///data.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)

intpk = Annotated[int, mapped_column(primary_key=True)]


class Model(DeclarativeBase):
    pass


class AuthTable(Model):
    __tablename__ = "Auth"

    id: Mapped[intpk]
    username: Mapped[str]
    password: Mapped[str]


class OrganizationTable(Model):
    __tablename__ = "Organization"

    id: Mapped[intpk]
    username: Mapped[str]
    payment_account: Mapped[str]
    balance: Mapped[float]
    INN: Mapped[str]
    address: Mapped[str]

    employees: Mapped[list["EmployeeTable"]] = relationship(back_populates="organization")


class EmployeeTable(Model):
    __tablename__ = "Employee"

    id: Mapped[intpk]
    organization_id = mapped_column(ForeignKey("Organization.id", ondelete="CASCADE"))
    phone_number: Mapped[str]

    organization: Mapped["OrganizationTable"] = relationship(back_populates="employees")
    calls: Mapped[list["CallsTable"]] = relationship(back_populates="employee")


class CitiesTable(Model):
    __tablename__ = "Cities"

    id: Mapped[intpk]
    city: Mapped[str]
    daily_rate: Mapped[float]
    night_rate: Mapped[float]
    discount: Mapped[float]

    calls: Mapped[list["CallsTable"]] = relationship(back_populates="city")


class CallsTable(Model):
    __tablename__ = "Calls"

    id: Mapped[intpk]
    employee_id: Mapped[int] = mapped_column(ForeignKey("Employee.id", ondelete="CASCADE"))
    city_id: Mapped[int] = mapped_column(ForeignKey("Cities.id", ondelete="CASCADE"))
    datetime: Mapped[str]
    duration: Mapped[int]
    cost: Mapped[float]

    employee: Mapped["EmployeeTable"] = relationship(back_populates="calls")
    city: Mapped["CitiesTable"] = relationship(back_populates="calls")


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
