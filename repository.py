from database import new_session, ProvidersTable, ClientsTable, CallsTable, CitiesTable
from schemas import ProvidersAdd, ClientsAdd, CallsAdd, CitiesAdd
from sqlalchemy import select


class ProvidersRepository:
    @classmethod
    async def add_one(cls, data: ProvidersAdd) -> int:
        async with new_session() as session:
            providers_dict = data.model_dump()

            provider = ProvidersTable(**providers_dict)
            session.add(provider)
            await session.flush()
            await session.commit()
            return provider.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(ProvidersTable)
            result = await session.execute(query)
            provider_model = result.scalars().all()
            return provider_model


class ClientsRepository:
    @classmethod
    async def add_one(cls, data: ClientsAdd) -> int:
        async with new_session() as session:
            clients_dict = data.model_dump()

            client = ClientsTable(**clients_dict)
            session.add(client)
            await session.flush()
            await session.commit()
            return client.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(ClientsTable)
            result = await session.execute(query)
            client_model = result.scalars().all()
            return client_model


class CallsRepository:
    @classmethod
    async def add_one(cls, data: CallsAdd) -> int:
        async with new_session() as session:
            calls_dict = data.model_dump()

            call = CallsTable(**calls_dict)
            session.add(call)
            await session.flush()
            await session.commit()
            return call.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(CallsTable)
            result = await session.execute(query)
            call_model = result.scalars().all()
            return call_model


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


