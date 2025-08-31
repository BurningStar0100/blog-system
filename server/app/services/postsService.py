from turtle import position, title
from fastapi import HTTPException, status
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from sqlalchemy.orm.session import Session

from app.models.post import Post
from app.schemas.post import CreatePost


class PostsService: 
    def __init__(self):
        pass
    
    @staticmethod
    def delete_post_by_id_service(post_id: int, db: Session):
        post = PostsService.get_post_by_id(post_id, db)  # assuming this already raises if not found
        try:
            db.delete(post)
            db.commit()
            return {"message": f"Post with id {post_id} deleted successfully"}
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error deleting post: {str(e)}"
            )

    @staticmethod
    def get_post_by_id(post_id: int, db: Session):
        try:
            post = db.query(Post).filter(Post.id == post_id).one()
            return post
        except NoResultFound:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Post with id {post_id} not found"
            )
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Database error: {str(e)}"
            )
    @staticmethod
    def create_post_by_userId(user_id: int, post: CreatePost, db: Session):
        add_post = Post(
            title = post.title,
            user_id = user_id,
            content = post.content
        )
        db.add(add_post)
        db.commit()
        return add_post


        
        
