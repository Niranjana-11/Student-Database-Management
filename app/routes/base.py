from app.routes import (
    create_student,
    get_student,    
    delete_student,
    update_student,
)

from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(create_student.router,prefix="/students",tags=["Create Student"])
api_router.include_router(get_student.router,prefix="/students",tags=["Get Student"])   
api_router.include_router(delete_student.router,prefix="/students",tags=["Delete Student"])
api_router.include_router(update_student.router,prefix="/students",tags=["Update Student"])