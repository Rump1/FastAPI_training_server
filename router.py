from typing import Annotated

from fastapi import APIRouter, Depends
from repository import UsersRepository
from schemas import UsersAdd, Users

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@user_router.post("")
async def add_user(
        user: Annotated[UsersAdd, Depends()]
):
    user_id = await UsersRepository.add_one(user)
    return {"ok": True, "user_id": user_id}


@user_router.get("")
async def get_users():
    users = await UsersRepository.find_all()
    return users
