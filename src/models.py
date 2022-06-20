import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable = False)
    first_name = Column(String(250), nullable = False)
    last_name = Column(String(250), nullable = False)
    email = Column(String(250), nullable=False)
    post = relationship('Post', backref = 'users')
    user_from = relationship('Follower', backref = 'users')
    user_to = relationship('Follower', backref = 'users')
    comment = relationship('Comment', backref = 'users')

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key = True)
    users_id = Column(String(250), ForeignKey('users.id'))
    media_post = relationship('Media', backref = 'post')
    comment_post = relationship('Comment', backref = 'post')

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key = True)
    user_from_id = Column(Integer, ForeignKey('users.id'))
    user_to_id = Column(Integer, ForeignKey('users.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key = True)
    type = Column(String(50), nullable = False)
    url = Column(String(200), unique = True, nullable = False)
    post_id = Column(Integer, ForeignKey('post.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key = True)
    comment_text = Column(String(400), nullable = False)
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e