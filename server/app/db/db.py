import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm.session import Session
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URI = os.getenv("SUPABASE_URI")

engine = create_engine(SUPABASE_URI)

def get_session():
    with Session(engine) as session:
        yield session
class Base(DeclarativeBase):
    pass

def create_db_and_tables():
    from app.models.users import User
    Base.metadata.create_all(engine)