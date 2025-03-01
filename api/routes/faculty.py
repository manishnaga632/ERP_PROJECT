from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas.faculty import FacultyBase, FacultyResponse
from api.crud.faculty import create_faculty, get_all_faculties, update_faculty, delete_faculty

# Faculty API Router
router = APIRouter()

# ✅ Add New Faculty
@router.post("/add", response_model=FacultyResponse)
def add_faculty(faculty: FacultyBase, db: Session = Depends(get_db)):
    return create_faculty(db, faculty)

# ✅ Get All Faculties
@router.get("/all", response_model=list[FacultyResponse])
def get_faculties(db: Session = Depends(get_db)):
    return get_all_faculties(db)

# ✅ Update Faculty
@router.put("/update", response_model=FacultyResponse)
def update(faculty_id: int, faculty_data: FacultyBase, db: Session = Depends(get_db)):
    return update_faculty(db, faculty_id, faculty_data)

# ✅ Delete Faculty
@router.delete("/delete")
def delete(faculty_id: int, db: Session = Depends(get_db)):
    return delete_faculty(db, faculty_id)
