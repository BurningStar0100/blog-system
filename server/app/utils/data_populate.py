

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.orm.session import Session
from dotenv import load_dotenv
from typing import List

load_dotenv()

SUPABASE_URI = os.getenv("SUPABASE_URI")

engine = create_engine(SUPABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    with Session(engine) as session:
        yield session
class Base(DeclarativeBase):
    pass

def create_db_and_tables():
    from app.models.users import User
    Base.metadata.create_all(engine)

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import CascadeOptions, Mapped, mapped_column, relationship, relationships


class Post(Base):
    __tablename__ = "posts_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    content: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users_table.id"))
    
    users: Mapped["User"] = relationship(back_populates="posts")

class User(Base):
    __tablename__ = "users_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    user_name: Mapped[str] = mapped_column(String(30), unique=True)

    posts: Mapped[List["Post"]] = relationship(back_populates="users")

def populate_data():
    # Create tables (only if they don’t exist)
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()

    # --- Create Users ---
    users = [
        User(first_name="John", last_name="Doe", user_name="johnd"),
        User(first_name="Alice", last_name="Smith", user_name="alices"),
        User(first_name="Bob", last_name="Johnson", user_name="bobj"),
        User(first_name="Maria", last_name="Garcia", user_name="mariag"),
        User(first_name="David", last_name="Lee", user_name="davidl"),
    ]

    db.add_all(users)
    db.commit()

    # Refresh to get IDs
    for user in users:
        db.refresh(user)

    # --- Create Posts ---
    posts = [
        Post(title="FastAPI Intro", content="Learn the basics of FastAPI.", users=users[0]),
        Post(title="SQLAlchemy ORM Basics", content="Getting started with SQLAlchemy ORM.", users=users[0]),

        Post(title="Advanced FastAPI", content="Deep dive into FastAPI features.", users=users[1]),
        Post(title="Async in Python", content="How async works in Python.", users=users[1]),

        Post(title="Docker for Beginners", content="Containerize your first app.", users=users[2]),

        Post(title="Kubernetes 101", content="Intro to Kubernetes and pods.", users=users[3]),
        Post(title="Scaling FastAPI", content="How to scale FastAPI apps.", users=users[3]),

        Post(title="Postgres with SQLAlchemy", content="How to connect Postgres with SQLAlchemy.", users=users[4]),
    ]

    db.add_all(posts)
    db.commit()

    db.close()
    print("✅ Sample data populated successfully!")


if __name__ == "__main__":
    populate_data()
