from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse

from app.routes.post import post_router
from app.db.db import create_db_and_tables
from app.routes.user import user_router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def home():
    return RedirectResponse("/docs")

@app.get("/health")
def health(): 
    return JSONResponse(status_code=200, content={"status":"healthy"})

app.include_router(prefix="/post", router=post_router)
app.include_router(prefix="/user", router=user_router)
