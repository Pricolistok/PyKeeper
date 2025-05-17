from fastapi import FastAPI

from add_dishes_router import dishRouter
from init_DB import initDB

app = FastAPI()
initDB()
app.include_router(dishRouter)


def main():
    pass


if __name__ == '__main__':
    main()
