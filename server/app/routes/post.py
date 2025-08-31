from fastapi import APIRouter, Depends
from fastapi.routing import JSONResponse
from sqlalchemy.orm.session import Session

from app.db.db import get_session
from app.services.postsService import PostsService
from app.schemas.post import CreatePost, ResponsePost

post_router = APIRouter()

@post_router.get("/")
def postHome():
    return JSONResponse(status_code=200, content={"status":"Inside post router"})

@post_router.delete("/{post_id}")
def deletePostById(post_id: int, db: Session = Depends(get_session)):
    return PostsService.delete_post_by_id_service(post_id, db)

@post_router.get("/{post_id}")
def getPostById(post_id: int, db: Session = Depends(get_session)):
    return PostsService.get_post_by_id(post_id, db)

@post_router.post("/{user_id}", response_model=ResponsePost)
def createPostByUserId(user_id: int, post: CreatePost, db: Session = Depends(get_session)):
    return PostsService.create_post_by_userId(user_id, post, db);