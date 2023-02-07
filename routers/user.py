from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import user as db_user
from db.database import get_db
from schemas.user import UserBase, UserDisplay
from routers.utils import validate_email
from routers.exceptions import EmailValidationError

router = APIRouter(prefix="/user", tags=["user"])

# create user router
@router.post('/create', response_model=UserDisplay)
def create_user(user: UserBase, db: Session = Depends(get_db)):
    if not validate_email(user.email):
        raise EmailValidationError("Email is invalid")
    return db_user.create_user(user, db)