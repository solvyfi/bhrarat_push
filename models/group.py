from sqlite3 import Date
from unicodedata import category
from xmlrpc.client import DateTime
from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr
from typing import Optional, Any
from beanie import PydanticObjectId


class Group(Document):
    groupname: str
    Title: Optional[str]
    owner : list
    members : list 
    time_creation: int
    chat : Optional[dict]
    ques : Optional[list]
    profile_pic : Optional[str]
    metaData : Optional[dict] 
    chatter : Optional[str]
    ranking : Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "groupname": "Group no. xbh3j",
                "Title": "We are experts/interested in sports, especially Cricket and BasketBall.",
                "owner" : [],
                "members" : [],
                "time_creation" : 345434543, 
                "chat" : {
                    "chatter" : "Hi! Are you?",
                },
                "ques" : [],
                 "profile_pic" : "www.s3.solvyfi.com/53434" ,
                "metaData" : {
                    "ranking" : 8,
                }
            }
        }


class Res(BaseModel):
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


