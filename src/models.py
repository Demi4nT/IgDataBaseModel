import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    likeid = Column(Integer, ForeignKey('liked.id'))
    postid = Column(Integer, ForeignKey("post.id"))
    commentid = Column(Integer, ForeignKey("comment.id"))
    
    

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    content = Column(String(250), nullable=False)
    commentid=Column(Integer, ForeignKey('comment.id'))
    likeid = Column(Integer, ForeignKey("like.id"))
    user = relationship(User)
    

class Comment(Base):
    __tablename__ ='comment'
    id = Column(Integer, primary_key=True)
    content = Column(String(250), nullable=False)
    user = relationship(User)
    post = relationship(Post)

class Like(Base):
    __tablename__ ='like'
    id = Column(Integer, primary_key=True)
    post = relationship(Post)
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e