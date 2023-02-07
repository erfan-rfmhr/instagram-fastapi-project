from sqlalchemy.orm import Session
from db.hash import Hash
from db.models import User
from schemas.user import UserBase


def create_user(request: UserBase, db: Session):
    user = User(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password) # Hashed password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user