from sqlalchemy import Column, Integer, String, DateTime, func
from api.database.base import Base

class Faculty(Base):
    __tablename__ = "faculty"

    id = Column(Integer, primary_key=True, index=True)  # ✅ Primary Key
    name = Column(String(255), nullable=False)  # ✅ Faculty Name
    qualification = Column(String(255), nullable=False)  # ✅ Qualification
    dob = Column(String(50), nullable=False)  # ✅ Date of Birth
    mobile = Column(String(15), unique=True, nullable=False)  # ✅ Mobile Number
    gender = Column(String(10), nullable=False)  # ✅ Gender
    status = Column(String(50), default="active")  # ✅ Faculty Status
    created_at = Column(DateTime, nullable=False, default=func.now())  # ✅ Auto Timestamp
