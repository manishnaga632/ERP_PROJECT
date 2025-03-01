from sqlalchemy.orm import Session
from fastapi import HTTPException
from api.database.models.course import Course  # ✅ Correct import
from api.database.schemas.courses import CourseCreate, CourseUpdate  # ✅ Correct import

# ✅ Add New Course
def create_course(db: Session, course: CourseCreate):
    db_course = Course(  # ✅ Correct Model Name
        name=course.name,
        description=course.description,
        price=course.price,
        discount=course.discount,
        duration=course.duration,
        is_popular=course.is_popular,
        is_ondemand=course.is_ondemand,
        status=course.status
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

# ✅ Get All Courses
def get_all_courses(db: Session):
    return db.query(Course).all()  # ✅ Correct Model Name

# ✅ Update Course
def update_course(db: Session, course_id: int, course_data: CourseUpdate):
    course = db.query(Course).filter(Course.id == course_id).first()  # ✅ Correct Model Name
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Update only provided fields
    for key, value in course_data.dict(exclude_unset=True).items():
        setattr(course, key, value)
    
    db.commit()
    db.refresh(course)
    return course

# ✅ Delete Course
def delete_course(db: Session, course_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()  # ✅ Correct Model Name
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    db.delete(course)
    db.commit()
    return {"message": "Course deleted successfully"}
