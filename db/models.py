from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float,  DateTime
from settings.consts import MAXI_STR_NAME, MAXI_LEN_NAME_OF_DISH, MAXI_COMPOUND_OF_DISH, MAXI_RECEIPT

Base = declarative_base()

class OrdersBase(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    name_of_customer = Column(String(MAXI_STR_NAME))
    number_of_order = Column(Integer)
    time_of_order = Column(DateTime)


class Dishes(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True)
    name_of_dish = Column(String(MAXI_LEN_NAME_OF_DISH))
    compound_of_dish = Column(String(MAXI_COMPOUND_OF_DISH))
    receipt = Column(String(MAXI_RECEIPT))
    price = Column(Float)


class Merge(Base):
    __tablename__ = 'merge'

    id = Column(Integer, primary_key=True)
    order_number = Column(Integer)
    dish_id = Column(Integer)
    count = Column(Integer)
