from fastapi import APIRouter, Body

from database.database import *
from models.question import *

router = APIRouter()






#@router.post("/",response_model=Resp)
#async def create_question(question : Question = Body(...)):
#    question = await add_question(question)
#    return question



@router.post("/", response_description="Question data added into the database", response_model=Response)
async def add_question_data(question: Question = Body(...)):
    new_question = await add_question(question)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Student created successfully",
        "data": new_question
    }