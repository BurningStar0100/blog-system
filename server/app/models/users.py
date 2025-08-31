from typing import List, Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.db import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    user_name: Mapped[str] = mapped_column(String(30), unique=True)

    posts: Mapped[List["Post"]] = relationship(back_populates="users")

    
