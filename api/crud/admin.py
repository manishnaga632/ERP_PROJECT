from sqlalchemy.orm import Session
from api.database.models.admin import Admin

def authenticate_admin (db: Session, email: str, password: str):
   return db.query(Admin).filter(Admin.email == email, Admin.password == password).first()

