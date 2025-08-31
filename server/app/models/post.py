from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import CascadeOptions, Mapped, mapped_column, relationship, relationships
from app.db.db import Base

class Post(Base):
    __tablename__ = "posts_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    content: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users_table.id"))
    
    users: Mapped["User"] = relationship(back_populates="posts")
