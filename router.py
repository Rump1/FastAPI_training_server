from typing import Annotated

from fastapi import APIRouter, Depends
from repository import ProvidersRepository
from schemas import ProvidersAdd

providers_router = APIRouter(
    prefix="/providers",
    tags=["Providers"]
)


@providers_router.post("")
async def add_provider(
        user: Annotated[ProvidersAdd, Depends()]
):
    provider_id = await ProvidersRepository.add_one(user)
    return {"ok": True, "provider_id": provider_id}


@providers_router.get("")
async def get_providers():
    users = await ProvidersRepository.find_all()
    return users
