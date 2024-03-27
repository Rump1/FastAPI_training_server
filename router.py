from typing import Annotated

from fastapi import APIRouter, Depends
from repository import ProvidersRepository, ClientsRepository, CallsRepository, CitiesRepository
from schemas import ProvidersAdd, ClientsAdd, CallsAdd, CitiesAdd

providers_router = APIRouter(
    prefix="/providers",
    tags=["Providers"]
)


@providers_router.post("")
async def add_provider(
        provider: Annotated[ProvidersAdd, Depends()]
):
    provider_id = await ProvidersRepository.add_one(provider)
    return {"ok": True, "provider_id": provider_id}


@providers_router.get("")
async def get_providers():
    providers = await ProvidersRepository.find_all()
    return providers


clients_router = APIRouter(
    prefix="/clients",
    tags=["Clients"]
)


@clients_router.post("")
async def add_client(
        client: Annotated[ClientsAdd, Depends()]
):
    client_id = await ClientsRepository.add_one(client)
    return {"ok": True, "clients_id": client_id}


@clients_router.get("")
async def get_clients():
    clients = await ClientsRepository.find_all()
    return clients


calls_router = APIRouter(
    prefix="/calls",
    tags=["Calls"]
)


@calls_router.post("")
async def add_call(
        call: Annotated[CallsAdd, Depends()]
):
    call_id = await CallsRepository.add_one(call)
    return {"ok": True, "calls_id": call_id}


@calls_router.get("")
async def get_calls():
    calls = await CallsRepository.find_all()
    return calls


cities_router = APIRouter(
    prefix="/cities",
    tags=["Cities"]
)


@cities_router.post("")
async def add_city(
        city: Annotated[CitiesAdd, Depends()]
):
    city_id = await CitiesRepository.add_one(city)
    return {"ok": True, "cities_id": city_id}


@cities_router.get("")
async def get_cities():
    cities = await CitiesRepository.find_all()
    return cities
