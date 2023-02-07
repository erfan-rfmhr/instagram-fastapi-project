from datetime import datetime

from sqlalchemy.orm import Session

from db.models import Post
from schemas.post import PostBase


def create_post(request: PostBase, db: Session):
    post = Post(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        timestamp = datetime.now(),
        user_id = request.user_id,
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_all_posts(db: Session):
    return db.query(Post).all()