from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import post as db_post
from db.database import get_db
from schemas.post import PostBase, PostDisplay

router = APIRouter(prefix="/post", tags=["post"])

# create user router
@router.post('/create', response_model=PostDisplay)
def create_post(post: PostBase, db: Session = Depends(get_db)):
    return db_post.create_post(post, db)