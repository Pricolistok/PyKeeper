from sqlalchemy import create_engine
from db.models import Base

FILE_DB = 'sqlite:///orders.db'

engine = create_engine(FILE_DB, echo=True, future=True)

def initDB():
    Base.metadata.create_all(engine)
