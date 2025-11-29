from sqlalchemy import create_engine, URL
from sqlalchemy.orm import declarative_base, sessionmaker
from .config import Settings

engine = create_engine(url=URL.create(
    drivername='postgresql+psycopg2',
    host=Settings.DP_HOST,
    port=Settings.DP_PORT,
    database=Settings.DP_NAME,
    password=Settings.DP_PASS,
    username=Settings.DP_USER,
))
Base = declarative_base()

def get_db():
    return sessionmaker(engine)()