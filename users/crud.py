
from users.schemas import Create_User

def create_user(user_in:Create_User):
    user = user_in.model_dump()
    return {
        'success': True,
        'user': user,
    }
