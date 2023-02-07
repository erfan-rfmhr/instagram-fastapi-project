from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


# create user table
class User(Base):
    __tablename__ = "user"
    id = Column("id", Integer, primary_key=True, index=True, autoincrement=True, nullable=False, unique=True)
    username = Column("username", String(20), nullable=False, unique=True)
    email = Column("email", String, nullable=False)
    password = Column("password", String(16), nullable=False)
    posts = relationship("Post", back_populates="user")
    
    
# create post table
class Post(Base):
    __tablename__ = "post"
    id = Column("id", Integer, primary_key=True, index=True, autoincrement=True, nullable=False, unique=True)
    image_url = Column("image_url", String)
    image_url_type = Column("image_url_type", String)
    caption = Column("caption", String)
    timestamp = Column("timestamp", DateTime)
    user_id = Column("user_id", Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="posts")