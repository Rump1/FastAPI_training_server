# Файл для заполнения БД

from router import add_organization, add_city, add_employee, add_call, add_auth
from schemas import OrganizationAdd, CitiesAdd, EmployeeAdd, CallsAdd, AuthAdd
import random
from datetime import datetime

auths = {
    "Horns&Hooves": "deaad792606928825c0bf85cd46e9edf",
    "GoodBoys": "deaad792606928825c0bf85cd46e9edf",
    "Loopa": "deaad792606928825c0bf85cd46e9edf"
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

employee_amount = 20
calls_amount = 100


class DataBaseFiller:
    @classmethod
    async def database_filling(cls):
        for auth in auths:
            await add_auth(AuthAdd(username=auth, password=auths[auth]))

        for auth in auths:
            payment_account = str(random.randint(100000000000, 999999999999))
            balance = round(random.random() * 1000 + 5000, 2)
            INN = str(random.randint(100000000000, 999999999999))
            address = random.choice(addresses) + " " + str(random.randint(1, 99))

            await add_organization(OrganizationAdd(username=auth, payment_account=payment_account,
                                                   balance=balance, INN=INN, address=address))

        for city in cities:
            await add_city(CitiesAdd(city=city, daily_rate=cities[city]["daily_rate"],
                                     night_rate=cities[city]["night_rate"], discount=cities[city]["discount"]))

        for i in range(employee_amount):
            organization_id = random.randint(1, 3)
            phone_number = "8912" + str(random.randint(1000000, 9999999))

            await add_employee(EmployeeAdd(organization_id=organization_id, phone_number=phone_number))

        for i in range(calls_amount):
            employee_id = random.randint(1, employee_amount)
            city = random.choice(list(cities.keys()))
            format = "%Y-%m-%d %H:%M:%S"
            date = datetime.fromtimestamp(datetime.now().timestamp() - random.randint(1, 100000))
            duration = random.randint(1, 500)
            if date.hour <= 20 & date.hour >= 8:
                cost = duration * cities[city]["daily_rate"]
            else:
                cost = duration * cities[city]["night_rate"]
            if duration >= 300:
                cost = cost * (1 - cities[city]["discount"])
            cost = round(cost, 2)
            await add_call(CallsAdd(employee_id=employee_id, city_id=list(cities.keys()).index(city) + 1,
                                    datetime=date.strftime(format), duration=duration, cost=cost))


        
