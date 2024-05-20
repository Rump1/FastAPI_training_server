from typing import Annotated

from fastapi import APIRouter, Depends
from repository import OrganizationRepository, EmployeeRepository, CallsRepository, CitiesRepository, AuthRepository
from schemas import EmployeeAdd, CallsAdd, CitiesAdd, OrganizationAdd, AuthAdd


auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@auth_router.post("")
async def add_auth(
        auth: Annotated[AuthAdd, Depends()]
):
    auth_id = await AuthRepository.add_one(auth)
    return {"ok": True, "auth_id": auth_id}


@auth_router.get("")
async def get_auths():
    auths = await AuthRepository.find_all()
    return auths


organization_router = APIRouter(
    prefix="/organization",
    tags=["Organization"]
)


@organization_router.post("")
async def add_organization(
        organization: Annotated[OrganizationAdd, Depends()]
):
    organization_id = await OrganizationRepository.add_one(organization)
    return {"ok": True, "organization_id": organization_id}


@organization_router.get("")
async def get_organizations():
    organizations = await OrganizationRepository.find_all()
    return organizations


@organization_router.get("/{org_name}")
async def get_organizations(org_name: str):
    organization = await OrganizationRepository.find_org(org_name)
    return organization


employee_router = APIRouter(
    prefix="/employee",
    tags=["Employee"]
)


@employee_router.post("")
async def add_employee(
        employee: Annotated[EmployeeAdd, Depends()]
):
    employee_id = await EmployeeRepository.add_one(employee)
    return {"ok": True, "employee_id": employee_id}


@employee_router.get("")
async def get_employee():
    employees = await EmployeeRepository.find_all()
    return employees


@employee_router.get("/calls/{org_id}")
async def get_employee_with_calls(org_id: int):
    employees = await EmployeeRepository.find_organization_employees(org_id)
    return employees


calls_router = APIRouter(
    prefix="/calls",
    tags=["Calls"]
)


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


@calls_router.post("")
async def add_call(
        call: Annotated[CallsAdd, Depends()]
):
    current_balance = await CallsRepository.add_one(call)
    return {"ok": True, "current_balance": current_balance}


@calls_router.get("")
async def get_calls():
    calls = await CallsRepository.find_all()
    return calls
