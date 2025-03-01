from sqlalchemy import Column, Integer, String, Date, DateTime, Enum, func
from api.database.base import Base
from datetime import date, datetime  # ✅ Importing date & datetime

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)  # Primary Key ✅
    name = Column(String(255), unique=True, index=True, nullable=False)
    father_name = Column(String(255), nullable=False)
    mother_name = Column(String(255), nullable=False)
    dob = Column(Date, nullable=False)  # Date type better rahega
    mobile = Column(String(15), nullable=False)  # Mobile number ke liye size limit
    father_mobile = Column(String(15), nullable=False)
    gender = Column(Enum("Male", "Female", name="gender_enum"), nullable=False)  # ✅ Direct ENUM
    status = Column(String(20), nullable=False, default="active")  # Default status
    created_at = Column(DateTime, nullable=False, default=func.now())  # Auto timestamp
 