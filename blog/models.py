from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Blog(Base):
    __tablename__ = 'blogs' 
    id  = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    author = Column(String(100))
    topic = Column(String(100))
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("User", back_populates='blogs')

class User(Base):
    __tablename__ = 'users'
    id  = Column(Integer, primary_key=True, index=True)
    email = Column(String(100))
    username = Column(String(100))
    password = Column(String(200))
    blogs = relationship("Blog", back_populates='creator')



