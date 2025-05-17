from sqlalchemy.orm import Session
from consts import MAXI_LEN_NAME_OF_DISH, MAXI_COMPOUND_OF_DISH, MAXI_RECEIPT
from errors import ERROR_LEN_NAME_OF_DISH, ERROR_LEN_RECEIPT_OF_DISH, ERROR_LEN_COMPOUND_OF_DISH, ERROR_PRICE, OK
from database import Dishes
from init_DB import engine
from fastapi import HTTPException


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


def validate_new_dish(name: str, compound: str, receipt: str, price: str):
    if not validate_name(name):
        return ERROR_LEN_NAME_OF_DISH
    if not validate_compound(compound):
        return ERROR_LEN_COMPOUND_OF_DISH
    if not validate_receipt(receipt):
        return ERROR_LEN_RECEIPT_OF_DISH
    if not validate_price(price):
        return ERROR_PRICE

    return OK


def validate_name(name: str):
    return 0 < len(name) <= MAXI_LEN_NAME_OF_DISH


def validate_compound(compound: str):
    return 0 < len(compound) <= MAXI_COMPOUND_OF_DISH


def validate_receipt(receipt: str):
    return 0 < len(receipt) <= MAXI_RECEIPT


def validate_price(price: str):
    try:
        price = float(price)
        if price < 0:
            return False
        return True
    except ValueError:
        return False
