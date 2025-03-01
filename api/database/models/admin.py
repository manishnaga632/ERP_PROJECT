from sqlalchemy import Column, Integer, String
from api.database.base import Base

class Admin(Base):
    __tablename__ = "admin"  # Plural name is better for consistency

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)  
    password = Column(String(255), nullable=False)  

  



