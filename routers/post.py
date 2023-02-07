from fastapi import APIRouter, Depends, UploadFile, File, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
import secrets
import shutil

from db import post as db_post
from db.database import get_db
from schemas.post import PostBase, PostDisplay

router = APIRouter(prefix="/post", tags=["post"])

# create post endpoint
@router.post('/create-by-url', response_model=PostDisplay)
def create_post(post: PostBase, db: Session = Depends(get_db)):
    return db_post.create_post(post, db)

# get posts
@router.get("/get-all", response_model=list[PostDisplay])
def get_posts(db: Session = Depends(get_db)):
    return db_post.get_all_posts(db)

# upload file
@router.post("/create-by-upload-image")
def upload_post(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.content_type in ("image/jpeg", ("image/png")):
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="File type must be jpeg or png"
        )
    
    new_name = secrets.token_hex(8)
    _, file_ext = file.filename.split('.')
    filename = new_name + file_ext
    
    with open(f"uploaded-images/{filename}", 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)