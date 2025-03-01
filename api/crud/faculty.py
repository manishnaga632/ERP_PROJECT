from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.database.models.faculty import Faculty
from api.database.schemas.faculty import FacultyBase

# ✅ Add New Faculty
def create_faculty(db: Session, faculty: FacultyBase):
    db_faculty = Faculty(
        name=faculty.name,
        qualification=faculty.qualification,
        dob=faculty.dob,
        mobile=faculty.mobile,
        gender=faculty.gender,
        status=faculty.status
    )
    db.add(db_faculty)
    db.commit()
    db.refresh(db_faculty)
    return db_faculty

# ✅ Get All Faculties
def get_all_faculties(db: Session):
    return db.query(Faculty).all()

# ✅ Update Faculty
def update_faculty(db: Session, faculty_id: int, faculty_data: FacultyBase):
    faculty = db.query(Faculty).filter(Faculty.id == faculty_id).first()
    if not faculty:
        raise HTTPException(status_code=404, detail="Faculty not found")

    faculty.name = faculty_data.name
    faculty.qualification = faculty_data.qualification
    faculty.dob = faculty_data.dob
    faculty.mobile = faculty_data.mobile
    faculty.gender = faculty_data.gender
    faculty.status = faculty_data.status

    db.commit()
    db.refresh(faculty)
    return faculty

# ✅ Delete Faculty
def delete_faculty(db: Session, faculty_id: int):
    faculty = db.query(Faculty).filter(Faculty.id == faculty_id).first()
    if not faculty:
        raise HTTPException(status_code=404, detail="Faculty not found")

    db.delete(faculty)
    db.commit()
    return {"message": "Faculty deleted successfully"}
