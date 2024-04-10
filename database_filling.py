# Файл для заполнения БД

from router import add_provider, add_city, add_client, add_call
from schemas import ProvidersAdd, CitiesAdd, ClientsAdd, CallsAdd
import random

# Providers:
providers = {
    "RTK": "99582bdd1cdaccd1a9a9251741f2bbcb4f66acf4ac36ba094138696958ed6a66",
    "TTK": "2e75e7cf2e16cd690cab0f9af9eae8a12facec0d194ca09fb6642c6cc8b63799",
    "DOM": "765308c19bcebac9f80ede96a985125a2c437066b9a03c5bb5bfe4407ef14c31"
}

cities = {
    "Москва": {
        "daily_rate": 0.1,
        "night_rate": 0.2,
        "discount": 0.1},
    "Пермь": {
        "daily_rate": 0.05,
        "night_rate": 0.1,
        "discount": 0.2},
    "Санкт-Петербург": {
        "daily_rate": 0.1,
        "night_rate": 0.2,
        "discount": 0.15},
    "Воронеж": {
        "daily_rate": 0.05,
        "night_rate": 0.1,
        "discount": 0.2},
    "Самара": {
        "daily_rate": 0.07,
        "night_rate": 0.14,
        "discount": 0.1},
    "Екатеринбург": {
        "daily_rate": 0.08,
        "night_rate": 0.16,
        "discount": 0.15}
}

addresses = ["Пушкина", "Ленина", "Екатерининская", "Грибоедова", "Революции", "Цветочная", "Мира", "Космонавтов"]

clients_amount = 20
calls_amount = 100


class DataBaseFiller:
    @classmethod
    async def database_filling(cls):
        for provider in providers:
            await add_provider(ProvidersAdd(login=provider, password=providers[provider]))

        for city in cities:
            await add_city(CitiesAdd(city=city, daily_rate=cities[city]["daily_rate"],
                                     night_rate=cities[city]["night_rate"], discount=cities[city]["discount"]))

        for i in range(clients_amount):
            provider_id = random.randint(1, 3)
            balance = round(random.random() * 1000, 2)
            phone_number = "8912" + str(random.randint(1000000, 9999999))
            INN = str(random.randint(100000000000, 999999999999))
            address = random.choice(addresses) + " " + str(random.randint(1, 99))

            await add_client(ClientsAdd(provider_id=provider_id, balance=balance,
                                        phone_number=phone_number, INN=INN, address=address))

        for i in range(calls_amount):
            client_id = random.randint(1, clients_amount)
            city = random.choice(list(cities.keys()))
            time_of_day = random.choice(["day", "night"])
            duration = random.randint(1, 500)
            if time_of_day == "day":
                cost = duration * cities[city]["daily_rate"]
            else:
                cost = duration * cities[city]["night_rate"]
            if duration >= 300:
                cost = cost * (1 - cities[city]["discount"])
            cost = round(cost, 2)
            await add_call(CallsAdd(client_id=client_id, city_id=list(cities.keys()).index(city) + 1,
                                    time_of_day=time_of_day, duration=duration, cost=cost))


        
