
from ..import schemas, models
from ..hashing import Hash
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException
from ..database import get_db
from fastapi import APIRouter
from ..repository import user
from ..oauth2 import get_current_user
router = APIRouter(
    prefix= '/user',
    tags=['users']
)


@router.post('',response_model=schemas.ShownUser)
def create_user(request : schemas.User, db : Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShownUser)
def get_user(id : int , db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return user.get_user_by_id(id, db)