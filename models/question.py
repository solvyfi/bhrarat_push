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
    req_part : int
    curr_part : Optional[int]
    bounty : float = 0.0 
    time_asked : str
    time_answered : Optional[str]
    likes : Optional[list]
    comment : Optional[dict]
    comment_text : Optional[str]
    commenter : Optional[str]
    vote : Optional[int]
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
                "target_responder" : [], # Public , GroupID or IndividualIDs
                "option" : [],
                "req_part" : "10",
                "curr_part" : "1",
                "bounty" : "9.99",
                "time_asked" : "time_asked",
                "time_answered" : "time_answered",
                "like" : [],
                "comment" : {
                    "commenter" : "john Doe",
                    "comment_text" : "That's a great comment! \m/",
                    "vote" : "0"
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