from fastapi import FastAPI
from api.routes import admin,Student,courses,faculty
from api.database.connection import engine
from api.database.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(admin.router, prefix="/Admin", tags=["Admin"])

app.include_router(Student.router, prefix="/Student", tags=["Student"])

app.include_router(courses.router, prefix="/courses", tags=["courses"])

app.include_router(faculty.router, prefix="/faculty", tags=["faculty"])


    