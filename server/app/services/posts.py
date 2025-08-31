from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import Update
from sqlalchemy.orm.session import Session

from app.models.post import Post
from app.schemas.posts import PostRequest, UpdatePostRequest
from app.models import post


def createPostByUserId(user_id, post_data : PostRequest, db: Session):
    post_content = Post(
        title = post_data.title,
        content = post_data.content,
        user_id = user_id
    )
    db.add(post_content)
    db.commit()

    return post_content

def getPostById(post_id:int, db: Session):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(
            status_code= 404,
            detail= f"The post with id {post_id} not found"
        )
    return post

def deletePostById(post_id:int, db: Session):
    post = getPostById(post_id,db)
    db.delete(post)
    db.commit()
    return JSONResponse(content=f"Successfully deleted post with id {post_id}")

def updatePostById(post_id:int , post_data : UpdatePostRequest, db: Session):
    try:
        # Get the existing post
        post = getPostById(post_id, db)
        updated = False

        if post_data.title is not None:
            post.title = post_data.title
            updated = True   
        if post_data.content is not None:
            post.content = post_data.content
            updated = True
        if not updated:
            raise HTTPException(
                status_code=400,
                detail="No valid fields provided for update"
            )
        db.commit()
        db.refresh(post)
        
        return post
        
    except HTTPException:
        # Re-raise HTTPExceptions (like 404 from getPostById)
        raise
    except Exception as e:
        # Rollback on any other error
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Failed to update post: {str(e)}"
        )
