from importlib.metadata import metadata
from sqlite3 import Date
from unicodedata import category
from xmlrpc.client import DateTime
from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr
from typing import Optional, Any
from beanie import PydanticObjectId


class Category(Document):
    categoryname : str
    Title : Optional[str]
    followers : list 
    ques : Optional[list]
    profile_pic : Optional[str]
    metadata : Optional[dict] 

    class Config:
        schema_extra = {
            "example": {
                "categoryname": "categoryname no. xbh3j",
                "Title" : "We are experts/interested in sports, especially Cricket and BasketBall.",
                "followers" : [],
                "ques" : [],
                "profile_pic" : "url",
                "metadata" : "Meta",
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


