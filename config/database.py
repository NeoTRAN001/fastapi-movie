import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

load_dotenv(".env")
database_url: str = f"mysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('HOST')}:3306/{os.getenv('DATABASE')}?ssl=true"
engine = create_engine(database_url)
Base = declarative_base()


def db_config():
    Base.metadata.create_all(bind=engine)
