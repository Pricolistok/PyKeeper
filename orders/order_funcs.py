from sqlalchemy.orm import Session
from datetime import datetime

from settings.errors import OK
from db.models import OrdersBase, Merge
from db.init_DB import engine
from orders.validate_order import validate_order


def add_orders_to_DB(name_of_customer: str, number_of_order: str, dishes: dict,  time_of_order: datetime):
    error_code = validate_order(name_of_customer, number_of_order, dishes)
    if error_code != OK:
        return error_code
    session = Session(engine)
    add_orders_to_session(name_of_customer, int(number_of_order), dishes, time_of_order, session)
    session.commit()
    session.close()
    return OK


def add_orders_to_session(name_of_customer: str, number_of_order: int,
                          dishes: dict,  time_of_order: datetime, session: Session):
    for i in dishes:
        merge = Merge(
            order_number=number_of_order,
            dish_id=int(i),
            count=int(dishes[i])
        )
        session.add(merge)
    order = OrdersBase(
        name_of_customer=name_of_customer,
        number_of_order=number_of_order,
        time_of_order=time_of_order,
    )
    session.add(order)

