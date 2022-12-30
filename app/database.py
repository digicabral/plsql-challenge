from enum import auto
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db?check_same_thread=False')

SessionLocal = sessionmaker(bind=engine)

#call the models
Base = declarative_base()

def get_db():
        db = SessionLocal()
        try:
                yield db
        finally:
                db.close()