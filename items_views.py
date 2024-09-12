from typing import Annotated

from fastapi import Path, APIRouter

items_router = APIRouter(prefix='/items')


@items_router.get("/")
async def get_item():
    return ["item1",
            "item2", "item3",
            ["item4", "item5", "item6"]]


@items_router.get("/{item_id}")
async def get_item(item_id: Annotated[int, Path(ge=1, le=1000)]):
    return {"item_id":
                {'id': item_id}}


@items_router.get("/latest/")
async def get_latest_item(latest_id: int = 0, id: int = None):
    return {"id": id, "name": "latest item"}
