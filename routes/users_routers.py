from fastapi import APIRouter

from db.user import createUser, checkUser
from models.model import UserSchema, UserLoginSchema

from auth.auth_handler import signJWT
from fastapi.responses import JSONResponse

users_routes = APIRouter()

# salt = "xzfX9364"

@users_routes.post("/signup", tags=["users"])
def create_user(user: UserSchema):
    flag = createUser(user.full_name, user.email, user.password)

    if flag == 0:
        return JSONResponse(content="Error!", status_code=500)

    else:

        return JSONResponse(content="Add user successful", status_code=201)


@users_routes.post("/login", tags=["users"])
def user_login(user: UserLoginSchema):
    if checkUser(user.email, user.password):
        return signJWT(user.email)
    return JSONResponse(content="Wrong login details!", status_code=500)
