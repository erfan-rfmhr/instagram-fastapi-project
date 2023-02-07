from fastapi import FastAPI

from db.database import engin
from db.models import Base
from routers import user

Base.metadata.create_all(engin)

app = FastAPI()
app.include_router(user.router)

@app.get('/')
def home():
    return "Instagram project"