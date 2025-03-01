from sqlalchemy.orm import Session
from api.database.models.Student import  Student
from api.database.schemas.Student import StudentCreate ,StudentUpdate ,StudentResponse
from fastapi import HTTPException
from typing import List

def create_student(db: Session, student: StudentCreate):
    db_student = Student(
        name=student.name,
        father_name=student.father_name,
        mother_name=student.mother_name,  
        dob=student.dob,
        mobile=student.mobile,
        father_mobile=student.father_mobile,
        gender=student.gender, 
        created_at=student.created_at
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student  


def update_student(db: Session, student_id: int, student_data: StudentUpdate):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Update only the fields that are provided in the request
    for key, value in student_data.dict(exclude_unset=True).items():
        setattr(student, key, value)
    
    db.commit()
    db.refresh(student)
    return student


def get_all_students(db: Session) -> List[StudentResponse]:
    students = db.query(Student).all()
    return students