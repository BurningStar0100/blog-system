from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session

from app.db.db import get_session
from app.models.users import User
from app.services.users import getUserPostById

user_router = APIRouter()

@user_router.get("/{user_id}")
def get_user_posts(user_id: int, db: Session = Depends(get_session)):
    return getUserPostById(user_id, db)

