from sqlalchemy.orm import Session
from datetime import datetime

from settings.consts import MAXI_STR_NAME
from settings.errors import ERROR_NAME_OF_CUSTOMER, ERROR_NUMBER_OF_ORDER, ERROR_DISH_ID, OK
from db.init_DB import engine
from db.models import Dishes


def validate_order(name_of_customer: str, number_of_order: str, dishes: dict):
    if not validate_name_of_customer(name_of_customer):
        return ERROR_NAME_OF_CUSTOMER
    if not validate_number_of_order(number_of_order):
        return ERROR_NUMBER_OF_ORDER
    if not validate_id_dishes(dishes):
        return ERROR_DISH_ID
    return OK


def validate_name_of_customer(name_of_customer: str):
    return 0 < len(name_of_customer) <= MAXI_STR_NAME


def validate_number_of_order(number: str):
    try:
        number = int(number)
        if number < 0 or number > 1000:
            return False
        return True
    except ValueError:
        return False


def get_cnt_dishes_from_db():
    session = Session(engine)
    cnt_dishes = len(session.query(Dishes).all())
    session.close()
    return cnt_dishes


def validate_id_dishes(dishes: dict):
    cnt_dishes_in_DB = get_cnt_dishes_from_db()
    try:
        print(cnt_dishes_in_DB)
        for i in dishes:
            id_dish = int(i)
            cnt_dish = int(dishes[i])
            print(id_dish, cnt_dish)
            if id_dish < 0 or id_dish > cnt_dishes_in_DB:
                return False
            if cnt_dish <= 0 or cnt_dish > 1000:
                return False
        return True
    except ValueError:
        return False
