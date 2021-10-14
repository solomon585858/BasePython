from fastapi import FastAPI, Depends

import crud
from dependencies import get_user_by_token
from schemas import UserIn, UserOut, User

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello world!!!"}


@app.get("/ping/")
def read_root():
    return {"message": "pong"}


@app.get("/users/me/", response_model=UserOut)
def get_me(user: User = Depends(get_user_by_token)):
    return user


@app.post("/users/", response_model=UserOut)
def create_user(user_in: UserIn):
    user = crud.create_user(user_in)
    return user


@app.get("/users/", response_model=list[UserOut])
def get_users():
    users = crud.list_users()
    return users
