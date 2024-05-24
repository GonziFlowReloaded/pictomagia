from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

def connection():
    engine = create_engine(
        f"mysql+pymysql://{os.getenv('SQL_USER')}:{os.getenv('SQL_PASSWORD')}@{os.getenv('SQL_HOST')}:{os.getenv('SQL_PORT')}/{os.getenv('SQL_DATABASE')}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def get_db():
    db = connection()
    try:
        yield db
    finally:
        db.close()
