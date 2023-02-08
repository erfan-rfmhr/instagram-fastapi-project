import secrets
import shutil

from fastapi import APIRouter, Depends, File, UploadFile, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from auth import login_manager
from db import post as db_post
from db.database import get_db
from schemas.post import PostBase, PostDisplay

router = APIRouter(prefix="/post", tags=["post"])


# get posts
@router.get("/get-all", response_model=list[PostDisplay])
def get_posts(db: Session = Depends(get_db), current_user = Depends(login_manager)):
    return db_post.get_all_posts(db)

# create post endpoint
@router.post('/create-by-url', response_model=PostDisplay)
def create_post(post: PostBase, db: Session = Depends(get_db), current_user = Depends(login_manager)):
    return db_post.create_post(post, db)
# upload file
@router.post(
    "/create-by-upload-image",
    response_class=JSONResponse,
    responses={
        415:{"content":{"application/json":{"example":"File type must be jpeg or png"}}, "description":"Just jpeg and png files are allowed"},
        200:{"content":{"application/json":{"example":"file.png"}}, "description":"Uploaded file name in static folder"},
    }
)
def upload_post(file: UploadFile = File(...), db: Session = Depends(get_db), current_user = Depends(login_manager)):
    if not file.content_type in ("image/jpeg", ("image/png")):
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="File type must be jpeg or png",
        )
    
    new_name = secrets.token_hex(8)
    _, file_ext = file.filename.split('.')
    filename = new_name + '.' + file_ext
    
    with open(f"uploaded-images/{filename}", 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return filename