from fastapi import APIRouter, Body

from database.database import *
from models.category import *


router = APIRouter()



@router.post("/", response_description="New category created.", response_model=Res)
async def add_category_data(category: Category = Body(...)):
    new_category = await add_category(category)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Student created successfully",
        "data": new_category
    }