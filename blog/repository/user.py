from ..hashing import Hash
from .. import models, schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def create(request : schemas.User, db : Session):
    encrypter = Hash()
    hashed_password = encrypter.hash(password= request.password)
    new_user = models.User(username = request.username, email = request.email, password = hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_id(id : int, db : Session):

    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"User {id} not found at all!")
    return user