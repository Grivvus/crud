import sqlalchemy
from sqlalchemy.orm import Session
import psycopg2

from models import Note

path_str = 'postgresql+pg8000://postgres:hackme@0.0.0.0/postgres'

def get_db_session():
    return Session(_get_db_engine())


def _get_db_engine():
    path = 'postgresql+pg8000://postgres:hackme@0.0.0.0/postgres'
    engine = sqlalchemy.create_engine(path, echo=True)
    return engine