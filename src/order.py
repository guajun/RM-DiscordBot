class Order:
    class Item:
        def __init__(self, name, price: dict, link: str = None) -> None:
            self.name = name
            self.price = price
            self.link = link

    class Review:
        import bson

        def __init__(self, r_d: bson.ObjectId, finance: bson.ObjectId) -> None:
            self.r_d = r_d
            self.finance = finance


    import bson

    def __init__(self, buyer: bson.ObjectId, items: list[dict], name: str = None, shipments: list[dict] = None, link: str = None) -> None:
        self.buyer = buyer
        self.items = items
        self.name = name
        self.shipments = shipments
        self.link = link
        self.status
        self.receipt
