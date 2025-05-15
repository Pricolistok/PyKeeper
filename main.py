from fastapi import FastAPI


router = FastAPI()


@router.get('/')
def main_router():
    print("OK")


def main():
    pass


if __name__ == '__main__':
    main()