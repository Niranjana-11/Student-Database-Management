from datetime import date
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from app import model  # noqa: F401  (makes sure the Student table is registered)
from app.database import Base, SessionLocal, engine
from app.model import Student
from app.routes.ai_query import router as ai_query_router
from app.routes.base import api_router

BASE_DIR = Path(__file__).resolve().parent

# Create tables if they do not exist yet
Base.metadata.create_all(bind=engine)


def seed_data() -> None:
    """Add a few sample students when the table is empty (keeps the live demo from looking blank)."""
    db = SessionLocal()
    try:
        if db.query(Student).count() == 0:
            db.add_all([
                Student(student_name="Asha Nair", student_class="10", student_section="A",
                        student_dob=date(2009, 5, 14), student_sub="Mathematics"),
                Student(student_name="Rahul Menon", student_class="9", student_section="B",
                        student_dob=date(2010, 8, 2), student_sub="Science"),
                Student(student_name="Meera Joseph", student_class="10", student_section="B",
                        student_dob=date(2009, 11, 21), student_sub="English"),
            ])
            db.commit()
    finally:
        db.close()


seed_data()

app = FastAPI(
    title="Student Management System",
    description="This is a simple student management system built using FastAPI and SQLite ORM.",
    version="1.0.0",
)

# API routes
app.include_router(api_router)
app.include_router(ai_query_router)

# Web interface served at /ui/
app.mount("/ui", StaticFiles(directory=BASE_DIR / "Frontend", html=True), name="ui")


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/ui/")























# from fastapi import FastAPI
# from app.database import Base,engine
# from app.routes.base import api_router
# from app.routes.ai_query import router as ai_query_router

# Base.metadata.create_all(bind=engine)
# app=FastAPI(
#     title="Student Management System",
#     description="This is a simple student management system built using FastAPI and SQLite ORM.",
#     version="1.0.0"
# )

# app.include_router(api_router)
# app.include_router(ai_query_router)

# from fastapi.staticfiles import StaticFiles

# app.mount("/ui", StaticFiles(directory="Frontend", html=True), name="ui")

# @app.get("/",tags=["Root"])

# def root():
#     return {
#     "message":"Welcome to the Student Management System API!"
#     }