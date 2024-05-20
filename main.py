import uvicorn
from database_filling import DataBaseFiller
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import organization_router, employee_router, cities_router, calls_router, auth_router

host = "127.0.0.1"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    # await create_tables()
    # print("Соединение с базой данных установлено")
    # await DataBaseFiller.database_filling()
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(auth_router)
app.include_router(organization_router)
app.include_router(employee_router)
app.include_router(cities_router)
app.include_router(calls_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host=host)
    wait = input()
