from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import  status, HTTPException
def get_all_blogs(db : Session):
    blogs = db.query(models.Blog).all()
    return blogs


def insert_blog(db : Session, request : schemas.Blog):
    new_blog  = models.Blog(topic=request.topic, 
                            author = request.author,
                            name = request.name, 
                            published= request.published , user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_one_blog(id,db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found at all!")
    return blog

def delete_one_blog(id : int, db : Session):
    try:
        db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
        db.commit()
        return f"Blog {id} was deleted successfully"
    except:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found at all!")


def update(id : int, request : schemas.Blog,  db : Session):

    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Blog {id} not found at all!")

    blog.update(request.dict())
    db.commit()
    return {f'Blog {id} has been updated!'}
