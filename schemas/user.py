from pydantic import BaseModel, Field


# user base class
class UserBase(BaseModel):
    username: str = Field(max_length=20)
    email: str = Field(regex="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,63}")
    password: str = Field(max_length=16)
    
# user display class
class UserDisplay(BaseModel):
    username: str
    email: str