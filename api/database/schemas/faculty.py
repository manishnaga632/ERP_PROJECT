from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# ✅ Faculty create/update schema
class FacultyBase(BaseModel):
    name: str
    qualification: str
    dob: str
    mobile: str
    gender: str
    status: Optional[str] = "active"

class Config:
        from_attributes = True

class FacultyResponse(BaseModel):
    id: int  # ✅ ID ko sabse pehle rakha
    created_at: datetime 
    name: str
    qualification: str
    dob: str
    mobile: str
    gender: str
    status: str

class Config:
        from_attributes = True

# ✅ Faculty response schema
class FacultyResponse(FacultyBase):
    id: int
    created_at: datetime

class Config:
        from_attributes = True
