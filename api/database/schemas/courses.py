from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# ✅ Course create schema (Add ke liye)
class CourseCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float  # ✅ int → float me change kiya
    discount: Optional[float] = 0.0  # ✅ int → float me change kiya
    duration: str
    is_popular: Optional[bool] = False
    is_ondemand: Optional[bool] = False
    status: Optional[str] = "active"

class Config:
        from_attributes = True

# ✅ Course response schema (Get ke liye)
class CourseResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float  # ✅ int → float me change kiya
    discount: Optional[float]  # ✅ int → float me change kiya
    duration: str
    is_popular: Optional[bool]
    is_ondemand: Optional[bool]
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

# ✅ Course update schema (Update ke liye)
class CourseUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None  # ✅ int → float me change kiya
    discount: Optional[float] = None  # ✅ int → float me change kiya
    duration: Optional[str] = None
    is_popular: Optional[bool] = None
    is_ondemand: Optional[bool] = None
    status: Optional[str] = None

class Config:
        from_attributes = True
