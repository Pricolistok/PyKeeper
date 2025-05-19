from fastapi import APIRouter
from datetime import datetime
import json

from orders.order_funcs import add_orders_to_DB


ordersRouter = APIRouter(prefix='/orders')


@ordersRouter.post('/add_order')
def add_order(name_of_customer: str, number_of_order: str, dishes: dict):
    return add_orders_to_DB(name_of_customer, number_of_order, dishes,  datetime.now())