from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.Student import StudentCreate, StudentResponse, StudentUpdate,StudentListResponse
from api.crud.Student import create_student,update_student,get_all_students

# Create a new API router for handling student-related endpoints
router = APIRouter()

@router.post("/register", response_model=StudentResponse)
def add(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student)

@router.put("/update", response_model=StudentResponse)
def update(student_id: int, student: StudentUpdate, db: Session = Depends(get_db)):
    return update_student(db, student_id, student)

@router.get("/all", response_model=StudentListResponse)
def get_students(db: Session = Depends(get_db)):
    students = get_all_students(db)
    return {"students": students}
