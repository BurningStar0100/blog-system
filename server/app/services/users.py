from fastapi import HTTPException
from sqlalchemy.orm.session import Session

from app.models.users import User

def getUserPostById(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.posts
