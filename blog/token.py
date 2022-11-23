from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Union
from .schemas import TokenData


SECRET_KEY = '2453816370c7416cc9f6febe699c20e6439dd45e3d6122d27b09646423613d94'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1



def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token : str,  credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
  