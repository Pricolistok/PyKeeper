from fastapi import APIRouter
from add_dish import add_dish_to_DB

dishRouter = APIRouter(prefix='/dishes')

@dishRouter.get('/')
def main_router():
    return "HELLO"

@dishRouter.post('/add_dish')
def add_dish_to_menu(name: str, compound: str, receipt: str, price: str):
    return add_dish_to_DB(name, compound, receipt, price)

