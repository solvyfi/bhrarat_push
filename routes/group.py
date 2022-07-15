from fastapi import APIRouter, Body

from database.database import *
from models.group import *


router = APIRouter()



@router.post("/", response_description="New group created.", response_model=Res)
async def add_group_data(group: Group = Body(...)):
    new_group = await add_group(group)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Student created successfully",
        "data": new_group
    }