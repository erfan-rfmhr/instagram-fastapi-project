from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engin = create_engine("sqlite:///instagram.db", connect_args={"check_same_thread":False})
Base = declarative_base()

def get_db():
    session = sessionmaker(bind=engin)()
    try:
        yield session
    finally:
        session.close()