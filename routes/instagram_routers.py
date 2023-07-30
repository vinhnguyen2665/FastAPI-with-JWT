from fastapi import APIRouter, Depends
from models.model import PostSchema, UpdatePostSchema
from db.post import *
from auth.auth_bearer import JWTBearer
from fastapi.responses import JSONResponse

instagram_routers = APIRouter()


@instagram_routers.get("/", tags=["hello"])
def hello():
    return JSONResponse(content="Hello", status_code=200)


@instagram_routers.post("/post/", dependencies=[Depends(JWTBearer())], tags=["posts"])
def add_post(post: PostSchema):
    flag = addPost(post.UserId, post.PostTitle, post.PostCreateDate, post.PostContent)

    if flag == 0:

        return JSONResponse(content="Error", status_code=500)

    else:

        return JSONResponse(content="Post Added", status_code=201)


@instagram_routers.get("/post/", dependencies=[Depends(JWTBearer())], tags=["posts"])
def get_all_posts():
    posts = getAllPost()

    if posts == 0:

        return JSONResponse(content="Error", status_code=500)
    else:

        return JSONResponse(content=posts, status_code=200)


@instagram_routers.get("/post/{id}", dependencies=[Depends(JWTBearer())], tags=["posts"])
def get_id_post(id: int):
    post = getIdPost(id)

    if post == -99:

        return JSONResponse(content="Error", status_code=500)

    else:

        return JSONResponse(content=post, status_code=200)


@instagram_routers.delete("/post/{id}", dependencies=[Depends(JWTBearer())], tags=["posts"])
def delete_id_post(id: int):
    post = deleteIdPost(id)

    if post == 0:

        return JSONResponse(content="Error", status_code=500)

    else:

        return JSONResponse(content="Post deletion successful", status_code=200)


@instagram_routers.put("/post/", dependencies=[Depends(JWTBearer())], tags=["posts"])
def update_post(post: UpdatePostSchema):
    post = updatePost(post.UserId, post.PostId, post.PostTitle, post.PostContent)

    if post == 0:

        return JSONResponse(content="Error", status_code=500)

    else:

        return JSONResponse(content="Post update successful", status_code=200)
