from turtle import title
from pydantic import BaseModel


class CreatePost(BaseModel):
    title: str
    content: str
    

class ResponsePost(BaseModel):
    id: int
    user_id: int
    title: str
    content: str
    
    class Config():
        from_attributes: True


    