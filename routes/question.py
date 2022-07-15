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
    reqr : int = question.req_part 
    trspdr : int = len(question.target_responder)
    disc = "Minimum 3 participants required to answer the question. req_part = %d, 2<req_part<13 allowed only."  %(question.req_part)
    if reqr <3 :
        return {
        "status_code": 411,
        "response_type": "Invalid Value",
        "description": disc,
        "data": question
    }
    if reqr >12 :
        return {
        "status_code": 411,
        "response_type": "Invalid value",
        "description": disc,
        "data": question
    }








    new_question = await add_question(question)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Student created successfully",
        "data": new_question
    }