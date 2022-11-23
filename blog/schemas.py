from pydantic import BaseModel
from typing import Optional,List

class Blog(BaseModel):

    name: str
    author : str
    topic : str
    published : Optional[bool]
    class Config:
        orm_mode = True


class ShownUser(BaseModel):
    username : str
    email : str
    blogs : List[Blog]
    class Config:
        orm_mode = True


class ShowBlog(Blog):
    creator : ShownUser
    class Config:
        orm_mode = True


class User(BaseModel):
    username : str
    password : str
    email : str

class Login(BaseModel):
    username : str
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    email : Optional[str] = None