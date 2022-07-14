from beanie import PydanticObjectId
from fastapi import Body, APIRouter, HTTPException
from passlib.context import CryptContext
from fastapi import FastAPI, Depends
from auth.jwt_bearer import JWTBearer
from auth.jwt_handler import sign_jwt
from database.database import add_user, update_user_data ,add_question
from models.user import Respo, User, UserData, UserSignIn ,UpdateUserModel

router = APIRouter()
token_listener = JWTBearer()
hash_helper = CryptContext(schemes=["bcrypt"])


@router.post("/login")
async def user_login(user_credentials: UserSignIn = Body(...)):
    user_exists = await User.find_one(User.email == user_credentials.username)
    if user_exists:
        password = hash_helper.verify(
            user_credentials.password, user_exists.password)
        if password:
            return sign_jwt(user_credentials.username)

        raise HTTPException(
            status_code=403,
            detail="Incorrect email or password"
        )

    raise HTTPException(
        status_code=403,
        detail="Incorrect email or password"
    )


@router.post("/new", response_model=UserData)
async def user_signup(user: User = Body(...)):
    user_exists = await User.find_one(User.email == user.email)
    if user_exists:
        raise HTTPException(
            status_code=409,
            detail="User with email supplied already exists"
        )

    user.password = hash_helper.encrypt(user.password)
    new_user = await add_user(user)
    return new_user

@router.put("{id}", response_model=Respo, dependencies=[Depends(token_listener)])
async def update_user(id: PydanticObjectId, req: UpdateUserModel = Body(...)):
    updated_user = await update_user_data(id, req.dict())
    if updated_user:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "User with ID: {} updated".format(id),
            "data": update_user
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. User with ID: {} not found".format(id),
        "data": False
    }

