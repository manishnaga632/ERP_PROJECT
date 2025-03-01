from pydantic import BaseModel
from datetime import date, datetime
from typing import Literal,Optional,List

class StudentCreate(BaseModel):
    name: str
    father_name: str
    mother_name: str
    dob: date  # Date format better rahega
    mobile: str
    father_mobile: str
    gender: Literal["Male", "Female"]  # ✅ Only "Male" or "Female" allowed
    created_at: datetime  # ✅ DateTime format better hai

class StudentResponse(BaseModel):
    id: int
    name: str
    father_name: str
    mother_name: str
    dob: date
    mobile: str
    father_mobile: str
    gender: Literal["Male", "Female"]
    created_at: datetime

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    father_name: Optional[str] = None
    mother_name: Optional[str] = None
    dob: Optional[date] = None
    mobile: Optional[str] = None
    father_mobile: Optional[str] = None
    gender: Optional[Literal["Male", "Female"]] = None
    created_at: Optional[datetime] = None  # Agar timestamp update karna ho toh

    class Config:
        from_attributes = True


class StudentListResponse(BaseModel):
    students: List[StudentResponse]  # ✅ List of StudentResponse

    class Config:
        from_attributes = True
