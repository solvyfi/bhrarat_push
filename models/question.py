from sqlite3 import Date
from unicodedata import category
from xmlrpc.client import DateTime
from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr
from typing import Optional, Any
from beanie import PydanticObjectId




class Question(Document):
    question : str
    option : list
    context : Optional[str]
    target_responder : list
    max_part : int
    curr_part : Optional[int]
    bounty : float = 0.0 
    #option1 : str
    #option2 : str
    #option3 : str
    #option4 : str
    #option5 : str#2222s
    #option6 : str
    time_asked : str
    time_answered : Optional[str]
    likes : Optional[list]
    comment : Optional[dict]
    comment_text : Optional[str]
    commenter : Optional[str]#PydanticObjectId]
    share : Optional[list]
    category : Optional[list]
    tags : Optional[list]
    swarm_result : Optional[str]
    survey_result : Optional[list]
    final_responders : Optional[list]
    state : str

    class Config:
        schema_extra = {
            "example" : {
                "question" : "Type your question",
                "context" : "text",
                "target_responder" : [],
                "option" : [],
                "max_part" : "10",
                "curr_part" : "1",
                "bounty" : "9.99",
                "time_asked" : "time_asked",
                "time_answered" : "time_answered",
                #"option 1" : "option 1",
                #"option 2" : "option 1",
                #option 3" : "option 1",
                #"option 5" : "option 1",
                #"option 5" : "option 1",
                #"option 6" : "option 1",
                "like" : [],
                "comment" : {
                    "commenter" : "john Doe",
                    "comment_text" : "That's a great comment! \m/",
                },
                "share" : [],
                "category" : [],
                "tags" : [],
                "swarm_result" : "answer",
                "survey_result" : [],
                "final_responders" : [],
                "state" : "unanswered" 
            }
        }


class Resp(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data"
            }
        }

class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data"
            }
        }