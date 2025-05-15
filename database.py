from tkinter.font import names

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from datetime import datetime

from consts import MAXI_STR_OF_ORDER

Base = declarative_base()

class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    number_of_customer = Column(Integer)
    compound_of_order = Column(String(MAXI_STR_OF_ORDER))
    time_of_order = Column(DateTime)


engine = create_engine('sqlite:///sqlite3.db', echo=True, future=True)
Base.metadata.create_all(engine)

session = Session(engine)
order = Orders(number_of_customer=100, compound_of_order="Burger", time_of_order=datetime.now())
session.add(order)
session.commit()
session.close()
