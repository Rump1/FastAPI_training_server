from sqlalchemy.orm import joinedload

from database import new_session, OrganizationTable, EmployeeTable, CallsTable, CitiesTable, AuthTable
from schemas import OrganizationAdd, EmployeeAdd, CallsAdd, CitiesAdd, AuthAdd
from sqlalchemy import select


class AuthRepository:
    @classmethod
    async def add_one(cls, data: AuthAdd) -> int:
        async with new_session() as session:
            auth_dict = data.model_dump()

            auth = AuthTable(**auth_dict)
            session.add(auth)
            await session.flush()
            await session.commit()
            return auth.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(AuthTable)
            result = await session.execute(query)
            auth_model = result.scalars().all()
            return auth_model


class OrganizationRepository:
    @classmethod
    async def add_one(cls, data: OrganizationAdd) -> int:
        async with new_session() as session:
            organization_dict = data.model_dump()

            organization = OrganizationTable(**organization_dict)
            session.add(organization)
            await session.flush()
            await session.commit()
            return organization.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(OrganizationTable)
            result = await session.execute(query)
            organization_model = result.scalars().all()
            return organization_model

    @classmethod
    async def find_org(cls, org_name):
        async with new_session() as session:
            query = select(OrganizationTable).filter_by(username=org_name)
            result = await session.execute(query)
            organization_model = result.scalars().all()
            return organization_model

    @classmethod
    async def update_balance(cls, employee_id: int, cost: float):
        async with new_session() as session:
            employee = await session.get(EmployeeTable, employee_id)
            organization = await session.get(OrganizationTable, employee.organization_id)
            organization.balance = organization.balance - cost
            await session.flush()
            await session.commit()
            return organization.balance


class EmployeeRepository:
    @classmethod
    async def add_one(cls, data: EmployeeAdd) -> int:
        async with new_session() as session:
            employee_dict = data.model_dump()

            employee = EmployeeTable(**employee_dict)
            session.add(employee)
            await session.flush()
            await session.commit()
            return employee.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(EmployeeTable)
            result = await session.execute(query)
            employee_model = result.scalars().all()
            return employee_model

    @classmethod
    async def find_organization_employees(cls, org_id):
        async with new_session() as session:
            query = (
                select(
                    EmployeeTable
                ).filter_by(organization_id=org_id).options(joinedload(EmployeeTable.calls))
            )
            result = await session.execute(query)
            employee_model = result.unique().scalars().all()
            return employee_model


class CitiesRepository:
    @classmethod
    async def add_one(cls, data: CitiesAdd) -> int:
        async with new_session() as session:
            cities_dict = data.model_dump()

            city = CitiesTable(**cities_dict)
            session.add(city)
            await session.flush()
            await session.commit()
            return city.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(CitiesTable)
            result = await session.execute(query)
            city_model = result.scalars().all()
            return city_model


class CallsRepository:
    @classmethod
    async def add_one(cls, data: CallsAdd) -> int:
        async with new_session() as session:
            calls_dict = data.model_dump()
            call = CallsTable(**calls_dict)
            session.add(call)
            await session.flush()
            await session.commit()
            current_balance = await OrganizationRepository.update_balance(call.employee_id, call.cost)
            return current_balance

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(CallsTable)
            result = await session.execute(query)
            call_model = result.scalars().all()
            return call_model



