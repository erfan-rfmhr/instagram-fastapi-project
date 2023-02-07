from pydantic import BaseModel, Field


# user base class
class UserBase(BaseModel):
    username: str = Field(default=..., max_length=20)
    email: str
    password: str = Field(default=..., max_length=16)
    
# user display class
class UserDisplay(BaseModel):
    username: str
    email: str
    
    class Config:
        orm_mode = True