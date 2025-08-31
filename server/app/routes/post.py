from fastapi import APIRouter
from fastapi.routing import JSONResponse

post_router = APIRouter()

@post_router.get("/")
def postHome():
    return JSONResponse(status_code=200, content={"status":"Inside post router"})