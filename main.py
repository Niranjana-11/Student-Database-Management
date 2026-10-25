from fastapi import FastAPI
from app.database import Base,engine
from app.routes.base import api_router
from app.routes.ai_query import router as ai_query_router

Base.metadata.create_all(bind=engine)
app=FastAPI(
    title="Student Management System",
    description="This is a simple student management system built using FastAPI and SQLite ORM.",
    version="1.0.0"
)

app.include_router(api_router)
app.include_router(ai_query_router)

from fastapi.staticfiles import StaticFiles

app.mount("/ui", StaticFiles(directory="Frontend", html=True), name="ui")

@app.get("/",tags=["Root"])

def root():
    return {
    "message":"Welcome to the Student Management System API!"
    }