from pydantic import BaseModel


class UsersAdd(BaseModel):
    login: str
    password: str


class Users(UsersAdd):
    id: int
