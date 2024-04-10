from pydantic import BaseModel


class ProvidersAdd(BaseModel):
    """
    Класс, описывающий таблицу Providers
    Обязательные аргументы:

    login: логин пользователя

    password: пароль пользователя
    """
    login: str
    password: str


class Providers(ProvidersAdd):
    """
    Класс для работы с ОРМ с таблицей Providers
    Обязательные аргументы:

    id: id пользователя в таблице, первичный ключ
    """
    id: int


class ClientsAdd(BaseModel):
    """
    Класс, описывающий таблицу Clients
    Обязательные аргументы:

    provider_id: id провайдера, вторичный ключ к полю id в таблице Providers

    balance: баланс клиента

    phone_number: номер телефона клиента

    INN: ИНН клиента

    address: адресс клиента
    """
    provider_id: int
    balance: float
    phone_number: str
    INN: str
    address: str


class Clients(ClientsAdd):
    """
    Класс для работы с ОРМ с таблицей Clients
    Обязательные аргументы:

    id: id пользователя в таблице, первичный ключ
    """
    id: int


class CallsAdd(BaseModel):
    """
    Класс, описывающий таблицу Calls
    Обязательные аргументы:

    client_id: id клиента, вторичный ключ к полю id в таблице Clients

    city_id: id города, вторичный ключ к полю id таблицы Cities

    time_of_day: время суток, в которое совершен звонок

    duration: длительность звонка в секундах

    cost: стоимость звонка в рублях
    """
    client_id: int
    city_id: int
    time_of_day: str
    duration: int
    cost: float


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

    discount: скидка после 10-ти минут разговора
    """
    city: str
    daily_rate: float
    night_rate: float
    discount: float


class Cities(CitiesAdd):
    """
    Класс для работы с ОРМ с таблицей Users

    Обязательные аргументы:

    id: id города в таблице, первичный ключ
    """
    id: int
