from fastapi import FastAPI, Body
import uvicorn
from pydantic import EmailStr, BaseModel
from typing import Annotated
from items_views import items_router

app = FastAPI()
app.include_router(items_router)
class Create_User(BaseModel):
    name: str
    email: EmailStr



@app.get("/")
async def get_start():
    return {"message": "Hello World",
            "hello": "world"}


@app.get("/hello/")
async def get_hello(name: str = 'asdf'):
    name = name.capitalize()
    return {"hello": f"world {name}"}


@app.get("/calc/add")
async def get_calc(a: int = 0, b: int = 0):
    return {"a": a,
            "b": b,
            "sum": a + b}

@app.post('/user/')
async def create_user(user: Create_User):
    return {"email":
            {"email": user}}



if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
