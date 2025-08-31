from typing import Optional
from pydantic import BaseModel

class PostRequest(BaseModel):
    title : str
    content : str

class PostResponse(BaseModel):
    title : str
    content : str
    user_id : int
    id : int

    class Config:
        from_attributes = True

class UpdatePostRequest(BaseModel):
    title : Optional[str] = None
    content : Optional[str] = None
    