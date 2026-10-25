from typing import List
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.database import get_db
from app.model import Student
from app.schema import StudentResponse

router=APIRouter()

@router.get("/",response_model=List[StudentResponse],status_code=status.HTTP_200_OK)
def get_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = db.query(Student).offset(skip).limit(limit).all()
    return students

@router.get("/{student_id}",response_model=StudentResponse,status_code=status.HTTP_200_OK)
def get_student(student_id: int, db: Session = Depends(get_db)):
    students = db.query(Student).filter(Student.id == student_id).first()
    if not students:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with id {student_id} not found")
    return students   