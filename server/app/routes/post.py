from fastapi import APIRouter, Depends
from fastapi.routing import JSONResponse
from sqlalchemy.orm.session import Session
from app.db.db import get_session
from app.schemas.posts import PostRequest, PostResponse, UpdatePostRequest
from app.services.posts import createPostByUserId, getPostById, deletePostById, updatePostById
post_router = APIRouter()

@post_router.get("/")
def postHome():
    return JSONResponse(status_code=200, content={"status":"Inside post router"})

@post_router.post("/{user_id}" , response_model= PostResponse)
def post_by_userid(user_id:int, post_data : PostRequest, db:Session = Depends(get_session) ):
    return createPostByUserId(user_id, post_data, db)

@post_router.get("/{post_id}")
def  get_post(post_id : int, db : Session = Depends(get_session)):
    return getPostById(post_id,db)

@post_router.delete("/{post_id}")
def  delete_post(post_id : int, db : Session = Depends(get_session)):
    return deletePostById(post_id,db)

@post_router.put('/{post_id}',response_model=PostResponse)
def update_post(post_id :int, post_data : UpdatePostRequest, db: Session = Depends(get_session)):
    return updatePostById(post_id,post_data,db)

