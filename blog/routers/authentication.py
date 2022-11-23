from fastapi import APIRouter , Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import schemas, database, models
from ..hashing import Hash
from ..database import get_db
from .. import token

from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(
    tags=['Authentication'],
    prefix='/auth'
)

@router.post('/login')
def login(request : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    encrypter = Hash()
    user = db.query(models.User).filter(models.User.email == request.username).first()
    
    if not user:
        raise HTTPException('Invalidad CREDENTIALS', status_code=status.HTTP_404_NOT_FOUND)
    if not encrypter.verify(user.password, request.password):
        raise HTTPException('Invalidad CREDENTIALS', status_code=status.HTTP_404_NOT_FOUND)
        
    access_token_expires = token.timedelta(minutes= token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
