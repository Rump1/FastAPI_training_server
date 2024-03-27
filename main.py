from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import providers_router, clients_router, cities_router, calls_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищенна")
    await create_tables()
    print("База создана")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(providers_router)
app.include_router(clients_router)
app.include_router(cities_router)
app.include_router(calls_router)
