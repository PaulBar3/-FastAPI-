from fastapi import FastAPI, Body
import uvicorn
from pydantic import EmailStr, BaseModel

app = FastAPI()

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


@app.get("/items/")
async def get_item():
    return ["item1",
            "item2", "item3",
            ["item4", "item5", "item6"]]


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id":
            {'id': item_id}}


@app.get("/items/latest/")
async def get_latest_item(latest_id: int = 0, id: int = None):
    return {"id": id, "name": "latest item"}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
