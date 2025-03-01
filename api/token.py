from datetime import datetime, timedelta
from jose import  jwt
from fastapi.security import OAuth2PasswordBearer
from api.config import SECRET_KEY, ALGORITHM


from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

