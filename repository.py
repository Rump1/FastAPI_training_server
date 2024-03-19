from database import new_session, UsersTable
from schemas import UsersAdd, Users
from sqlalchemy import select


class UsersRepository:
    @classmethod
    async def add_one(cls, data: UsersAdd) -> int:
        async with new_session() as session:
            user_dict = data.model_dump()

            user = UsersTable(**user_dict)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id

    @classmethod
    async def find_all(cls) -> list[Users]:
        async with new_session() as session:
            query = select(UsersTable)
            result = await session.execute(query)
            user_models = result.scalars().all()
            user_schemas = [Users.model_validate(user_model) for user_model in user_models]
            return user_schemas


