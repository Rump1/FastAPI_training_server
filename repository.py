from database import new_session, ProvidersTable
from schemas import ProvidersAdd
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


