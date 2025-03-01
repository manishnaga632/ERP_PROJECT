from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from api.database.base import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)  # ✅ Primary Key
    name = Column(String(255), unique=True, index=True, nullable=False)  # ✅ Course Name
    description = Column(String(500), nullable=True)  # ✅ Course Description
    price = Column(Integer, nullable=False)  # ✅ Course Price
    discount = Column(Integer, default=0)  # ✅ Discount (Default: 0)
    duration = Column(String(50), nullable=False)  # ✅ Duration (e.g., "3 months")
    is_popular = Column(Boolean, default=False)  # ✅ Is the course popular?
    is_ondemand = Column(Boolean, default=False)  # ✅ Is the course on-demand?
    status = Column(String(20), nullable=False, default="active")  # ✅ Default status
    created_at = Column(DateTime, nullable=False, default=func.now())  # ✅ Auto Timestamp
