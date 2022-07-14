from sqlite3 import Date
from unicodedata import category
from xmlrpc.client import DateTime
from beanie import Document
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr
from typing import Optional, Any
from beanie import PydanticObjectId

class User(Document):
    fullname: str
    email: EmailStr
    password: str
    dob : str
    gender : str
    interest : list

    class Collection:
        name = "user"

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Type here",
                "email": "xyz@solvyfi.com",
                "password": "123",
                "dob" : "2008-09-15",
                "gender": "What better defines you",
                "interest" : []
            }
        }






class UserSignIn(HTTPBasicCredentials):
    class Config:
        schema_extra = {
            "example": {
                "username": "xyz@solvyfi.com",
                "password": "123"
            }
        }


class UserData(BaseModel):
    fullname: str
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Type here",
                "email": "xyz@solvyfi.com",
            }
        }

class UpdateUserModel(BaseModel):
    interest : list

    class Collection:
        name = "user"

    class Config:
        schema_extra = {
            "example": {
                "interest" : []
            }
        }

class Respo(BaseModel):
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