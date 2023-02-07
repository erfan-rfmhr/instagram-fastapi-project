from fastapi import FastAPI

from db.database import engin
from db.models import Base

app = FastAPI()

Base.metadata.create_all(engin)

@app.get('/')
def home():
    return "Instagram project"