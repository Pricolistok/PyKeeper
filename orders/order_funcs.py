from sqlalchemy.orm import Session
from datetime import datetime

from settings.errors import OK, ERROR_FINDER_ORDER
from db.models import OrdersBase, Merge, Dishes
from db.init_DB import engine
from orders.validate_order import validate_order


def add_orders_to_DB(name_of_customer: str, number_of_order: str, dishes: dict,  time_of_order: datetime):
    error_code = validate_order(name_of_customer, number_of_order, dishes)
    if error_code != OK:
        raise error_code
    session = Session(engine)
    add_orders_to_session(name_of_customer, int(number_of_order), dishes, time_of_order, session)
    session.commit()
    session.close()
    raise OK


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

def decode_one_dish(id_dish: int, session):
    return session.query(Dishes).filter(Dishes.id == id_dish).first().name_of_dish


def decode_dishes(compound):
    session = Session(engine)
    for i in compound:
        i['name_of_position'] = decode_one_dish(i['id_of_position'], session)
        del i['id_of_position']
    session.close()


def get_compound_of_order(number_of_order: int):
    session = Session(engine)
    compound = session.query(Merge).filter(Merge.order_number == number_of_order).all()
    session.close()
    compound = [{'id_of_position': i.dish_id, 'name_of_position': None, 'count': i.count} for i in compound]
    decode_dishes(compound)
    return compound


def get_all_orders_from_DB():
    session = Session(engine)
    orders = session.query(OrdersBase).all()
    session.close()
    result = []
    if orders is None:
        raise ERROR_FINDER_ORDER
    for order in orders:
        tmp = order.to_dict()
        tmp['compound'] = get_compound_of_order(tmp['number_of_order'])
        result.append(tmp)
    return result


def get_one_order_from_DB(number_of_order: int):
    session = Session(engine)
    order = session.query(OrdersBase).filter(OrdersBase.number_of_order == number_of_order).first()
    if order is None:
        raise ERROR_FINDER_ORDER
    session.close()
    order = order.to_dict()
    order['compound'] = get_compound_of_order(order['number_of_order'])
    return order

