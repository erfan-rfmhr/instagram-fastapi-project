from datetime import datetime

from pydantic import BaseModel

from schemas.user import UserDisplay


# post base class
class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    user_id: int
    
# post display class
class PostDisplay(BaseModel):
    id: int
    image_url: str 
    image_url_type: str 
    caption: str 
    timestamp: datetime
    user: UserDisplay
    class Config:
        orm_mode = True