from fastapi import APIRouter
from users import crud

from users.schemas import Create_User

router = APIRouter(prefix='/users')


@router.post('/')
async def create_user(user: Create_User):
    return crud.create_user(user_in=user)
