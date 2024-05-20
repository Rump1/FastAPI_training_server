from pydantic import BaseModel


class AuthAdd(BaseModel):
    """
    Класс, описывающий таблицу Auth
    Обязательные аргументы:

    username: логин пользователя

    password: пароль пользователя
    """
    username: str
    password: str


class Auth(AuthAdd):
    """
    Класс для работы с ОРМ с таблицей Auth
    Обязательные аргументы:

    id: id пользователя в таблице, первичный ключ
    """
    id: int


class OrganizationAdd(BaseModel):
    """
    Класс, описывающий таблицу Organization
    Обязательные аргументы:

    username: имя пользователя

    payment_account: номер расчетного счета

    balance: баланс

    INN: ИНН

    address: адресс
    """
    username: str
    payment_account: str
    balance: float
    INN: str
    address: str


class Organization(OrganizationAdd):
    """
    Класс для работы с ОРМ с таблицей Organization
    Обязательные аргументы:

    id: id пользователя в таблице, первичный ключ
    """
    id: int


class EmployeeAdd(BaseModel):
    """
    Класс, описывающий таблицу Employee
    Обязательные аргументы:

    organization_id: id организации, вторичный ключ к полю id в таблице Organization

    phone_number: номер телефона клиента
    """
    organization_id: int
    phone_number: str


class Employee(EmployeeAdd):
    """
    Класс для работы с ОРМ с таблицей Employee
    Обязательные аргументы:

    id: id пользователя в таблице, первичный ключ
    """
    id: int


class CitiesAdd(BaseModel):
    """
    Класс, описывающий таблицу Cities
    Обязательные аргументы:

    city: название города

    daily_rate: дневной тариф

    night_rate: ночной тариф

    discount: скидка после 10-ти минут разговора
    """
    city: str
    daily_rate: float
    night_rate: float
    discount: float


class Cities(CitiesAdd):
    """
    Класс для работы с ОРМ с таблицей Cities

    Обязательные аргументы:

    id: id города в таблице, первичный ключ
    """
    id: int


class CallsAdd(BaseModel):
    """
    Класс, описывающий таблицу Calls
    Обязательные аргументы:

    employee_id: id клиента, вторичный ключ к полю id в таблице Employee

    city_id: id города, вторичный ключ к полю id таблицы Cities

    datetime: дата, в которую совершен звонок

    duration: длительность звонка в секундах

    cost: стоимость звонка в рублях
    """
    employee_id: int
    city_id: int
    datetime: str
    duration: int
    cost: float


class Calls(CallsAdd):
    """
    Класс для работы с ОРМ с таблицей Calls

    Обязательные аргументы:

    id: id звонка в таблице, первичный ключ
    """
    id: int



