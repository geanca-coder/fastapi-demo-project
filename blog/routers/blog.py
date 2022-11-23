from fastapi import APIRouter
from .. import schemas, oauth2
from typing  import List
from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import blog

get_current_user = oauth2.get_current_user


router = APIRouter(
    tags=["blogs"],
    prefix = "/blog"
)


@router.get('', response_model = List[schemas.ShowBlog] )
def all(db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return blog.get_all_blogs(db)

@router.post('', status_code=status.HTTP_201_CREATED)
def create(request : schemas.Blog, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return blog.insert_blog(db=db,request=request)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model = schemas.ShowBlog)
def get_one_blog(id, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return blog.get_one_blog(id,db)



@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_one_blog(id : int , db : Session = Depends(get_db) , current_user : schemas.User = Depends(get_current_user)):
    return blog.delete_one_blog(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id : int , request : schemas.Blog, db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return blog.update(id= id,request=request, db=db )


