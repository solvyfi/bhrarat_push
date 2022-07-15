from fastapi import FastAPI, Depends

from auth.jwt_bearer import JWTBearer
from config.config import initiate_database
from routes.user import router as UserRouter
from routes.student import router as StudentRouter
from routes.question import router as QuestionRouter
from routes.group import router as GroupRouter
from routes.category import router as CategoryRouter

app = FastAPI()
#vipin test
token_listener = JWTBearer()


@app.on_event("startup")
async def start_database():
   await initiate_database()
   print("3")


#try1
@app.get("/", tags=["Root"])
async def read_root():
    print("4")
    return {"message": "Welcome to this fantastic app."}



app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(StudentRouter, tags=["Students"], prefix="/student", dependencies=[Depends(token_listener)])
app.include_router(QuestionRouter, tags=["Question"], prefix="/questions",dependencies=[Depends(token_listener)])
app.include_router(GroupRouter, tags=["Group"], prefix="/group",dependencies=[Depends(token_listener)])
app.include_router(CategoryRouter, tags=["Category"], prefix="/category",dependencies=[Depends(token_listener)])
#1234