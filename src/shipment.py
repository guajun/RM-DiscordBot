class Shipment:
    from enum import Enum

    class Destiny(Enum):
        WAREHOUSE = "Consolidation Warehouse"
        UNIVERSITY = "University"
        OTHER = "Other"

    import bson

    def __init__(self, destiny: Destiny, orders: list[bson.ObjectId], price: dict = None, consolidator: bson.ObjectId = None) -> None:
        self.destiny = destiny
        self.orders = orders
        self.price = price
        self.consolidator = consolidator

    def __getattribute__(self, name):
        if name == '__dict__':
            modified_dict = super().__getattribute__('__dict__').copy()
            modified_dict['destiny'] = self.destiny._value_
            return modified_dict
        return super().__getattribute__(name)
