from pydantic import BaseModel


class UsersAdd(BaseModel):
    """
    Класс, описывающий таблицу Users
    Обязательные аргументы:

    login: логин пользователя

    password: пароль пользователя
    """
    login: str
    password: str


class Users(UsersAdd):
    """
    Класс для работы с ОРМ с таблицей Users

    Обязательные аргументы:

    id: id пользователя в таблице, первичный ключ
    """
    id: int


class PersonalAccountAdd(BaseModel):
    """
    Класс, описывающий таблицу PersonalAccount
    Обязательные аргументы:

    balance: баланс пользователя

    phone_number: номер телефона пользователя

    INN: ИНН пользователя

    address: адресс пользователя
    """
    balance: float
    phone_number: str
    INN: str
    address: str


class PersonalAccount(PersonalAccountAdd):
    """
    Класс для работы с ОРМ с таблицей PersonalAccount

    Обязательные аргументы:

    id: id пользователя в таблице, первичный ключ, вторичный ключ к полю id в таблице Users
    """
    id: int


class CallsAdd(BaseModel):
    """
    Класс, описывающий таблицу Calls
    Обязательные аргументы:

    user_id: id пользователя, вторичный ключ к полю id в таблице Users

    duration: длительность звонка в секундах

    cost: стоимость звонка в рублях

    city_id: id города, вторичный ключ к полю id таблицы Cities
    """
    user_id: float
    duration: int
    cost: float
    city_id: str


class Calls(CallsAdd):
    """
    Класс для работы с ОРМ с таблицей Calls

    Обязательные аргументы:

    id: id звонка в таблице, первичный ключ
    """
    id: int


class CitiesAdd(BaseModel):
    """
    Класс, описывающий таблицу Cities
    Обязательные аргументы:

    city: название города

    daily_rate: дневной тариф

    night_rate: ночной тариф
    """
    city: str
    daily_rate: float
    night_rate: float


class Cities(CitiesAdd):
    """
    Класс для работы с ОРМ с таблицей Users

    Обязательные аргументы:

    id: id города в таблице, первичный ключ
    """
    id: int
