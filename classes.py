from dataclasses import dataclass
from datetime import datetime


@dataclass
class Item:
    name: str
    quantity: int


class Order:
    def __init__(self, name_of_customer: str, compound_of_order: [Item], number: int):
        self.name_of_customer: str = name_of_customer
        self.compound_of_order: [Item] = compound_of_order
        self.time_of_order: datetime = datetime.now()
        self.number: int = number