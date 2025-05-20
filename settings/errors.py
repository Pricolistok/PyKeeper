from fastapi import HTTPException

OK = HTTPException(status_code=200, detail="Ok!")
ERROR_LEN_NAME_OF_DISH = HTTPException(status_code=400, detail="Error! Name too long!")
ERROR_LEN_COMPOUND_OF_DISH = HTTPException(status_code=400, detail="Error! Compound of dish too long!")
ERROR_LEN_RECEIPT_OF_DISH = HTTPException(status_code=400, detail="Error! Receipt of dish too long!")
ERROR_PRICE_OF_DISH = HTTPException(status_code=400, detail="Error! Wrong price!")
ERROR_NAME_OF_CUSTOMER = HTTPException(status_code=400, detail="Error! Name of customer too long!")
ERROR_NUMBER_OF_ORDER = HTTPException(status_code=400, detail="Error! Wrong number of order!")
ERROR_DISH_ID = HTTPException(status_code=400, detail="Error! Wrong dish id!")
ERROR_NO_ORDERS = HTTPException(status_code=404, detail="Error! No orders!")
ERROR_FINDER_ORDER = HTTPException(status_code=404, detail="Error! Wrong number of order!")

