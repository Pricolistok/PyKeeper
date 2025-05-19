from fastapi import APIRouter
from dishes.dish_funcs import add_dish_to_DB

dishRouter = APIRouter(prefix='/dishes')

@dishRouter.post('/add_dish')
def add_dish(name: str, compound: str, receipt: str, price: str):
    return add_dish_to_DB(name, compound, receipt, price)

