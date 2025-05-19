from settings.errors import (ERROR_LEN_NAME_OF_DISH, ERROR_LEN_COMPOUND_OF_DISH,
                             ERROR_LEN_RECEIPT_OF_DISH, ERROR_PRICE_OF_DISH, OK)
from settings.consts import MAXI_LEN_NAME_OF_DISH, MAXI_COMPOUND_OF_DISH, MAXI_RECEIPT


def validate_new_dish(name: str, compound: str, receipt: str, price: str):
    if not validate_name(name):
        return ERROR_LEN_NAME_OF_DISH
    if not validate_compound(compound):
        return ERROR_LEN_COMPOUND_OF_DISH
    if not validate_receipt(receipt):
        return ERROR_LEN_RECEIPT_OF_DISH
    if not validate_price(price):
        return ERROR_PRICE_OF_DISH

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
