from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.database.connection import SessionLocal
from api.database.schemas.admin import AdminLogin, Token
from api.token import create_access_token
from api.crud.admin import authenticate_admin
from fastapi import HTTPException

router = APIRouter(prefix="/admin", tags=["Admin"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login", response_model=Token)
def login(admin_data: AdminLogin, db: Session = Depends(get_db)):
    admin = authenticate_admin(db, admin_data.email, admin_data.password)
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    access_token = create_access_token(data={"sub": admin.email})
    return {"access_token": access_token, "token_type": "bearer"}





