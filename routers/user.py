from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from sqlalchemy.orm import Session

from auth import login_manager
from db import user as db_user
from db.database import get_db
from db.hash import Hash
from routers.exceptions import EmailValidationError
from routers.utils import validate_email
from schemas.user import UserBase, UserDisplay

router = APIRouter(prefix="/user", tags=["user"])

# login user
@router.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db_user.get_user_by_username(form_data.username, db)
    
    if user is not None and Hash.verify(user.password, form_data.password):
        access_token = login_manager.create_access_token(
            data={"sub": user.username}
        )
        response = JSONResponse(content={"access-token": access_token, "token_type": "bearer"})
        login_manager.set_cookie(response=response, token=access_token)
        return response
    else:
        raise InvalidCredentialsException


# create user router
@router.post('/create', response_model=UserDisplay)
def create_user(user: UserBase, db: Session = Depends(get_db)):
    if not validate_email(user.email):
        raise EmailValidationError("Email is invalid")
    return db_user.create_user(user, db)