from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.courses import CourseCreate, CourseResponse, CourseUpdate
from api.crud.courses import create_course, get_all_courses, update_course, delete_course

# Course API Router
router = APIRouter()

# ✅ Add New Course
@router.post("/add", response_model=CourseResponse)
def add_course(course: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db, course)

# ✅ Get All Courses
@router.get("/all", response_model=list[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    return get_all_courses(db)

# ✅ Update Course
@router.put("/update", response_model=CourseResponse)
def update(course_id: int, course_data: CourseUpdate, db: Session = Depends(get_db)):
    return update_course(db, course_id, course_data)

# ✅ Delete Course
@router.delete("/delete")
def delete(course_id: int, db: Session = Depends(get_db)):
    return delete_course(db, course_id)
