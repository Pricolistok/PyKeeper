from fastapi import APIRouter
from datetime import datetime

from orders.order_funcs import add_orders_to_DB, get_all_orders_from_DB


ordersRouter = APIRouter(prefix='/orders')


@ordersRouter.post('/add_order')
def add_order(name_of_customer: str, number_of_order: str, dishes: dict):
    return add_orders_to_DB(name_of_customer, number_of_order, dishes,  datetime.now())


@ordersRouter.get('/gat_all_orders')
def get_all_orders():
    return get_all_orders_from_DB()