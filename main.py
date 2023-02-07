from fastapi import FastAPI

from db.database import engin
from db.models import Base
from routers import user, post

Base.metadata.create_all(engin)

app = FastAPI()
app.include_router(user.router)
app.include_router(post.router)

@app.get('/')
def home():
    return {"message":"Instagram project"}