from sqlalchemy import Column, Integer, String

from db.database import Base

# create user table
class User(Base):
    __tablename__ = "users"
    id = Column("id", Integer, primary_key=True, index=True, autoincrement=True, nullable=False, unique=True)
    username = Column("username", String(20), nullable=False, unique=True)
    email = Column("email", String, nullable=False)
    password = Column("password", String(16), nullable=False)