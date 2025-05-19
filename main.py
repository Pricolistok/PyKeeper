from fastapi import FastAPI

from dishes.dishes_router import dishRouter
from orders.orders_routers import ordersRouter
from db.init_DB import initDB

app = FastAPI()
initDB()
app.include_router(dishRouter)
app.include_router(ordersRouter)



def main():
    pass


if __name__ == '__main__':
    main()
