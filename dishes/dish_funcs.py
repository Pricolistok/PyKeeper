from sqlalchemy.orm import Session
from fastapi import HTTPException

from settings.errors import OK
from db.models import Dishes
from db.init_DB import engine
from dishes.validate_dish import validate_new_dish


def add_dish_to_DB(name: str, compound: str, receipt: str, price: str):
    session = Session(engine)
    error_code = validate_new_dish(name, compound, receipt, price)
    if error_code != OK:
        raise HTTPException(error_code)
    dish = create_dish(name, compound, receipt, float(price))
    session.add(dish)
    session.commit()
    raise HTTPException(200)


def create_dish(name: str, compound: str, receipt: str, price: float):
    return Dishes(
        name_of_dish=name,
        compound_of_dish=compound,
        receipt=receipt,
        price=price
    )
