class Price:
    from enum import Enum
    class CurrencyCode(Enum):
        HKD = "HKD"
        CNY = "CNY"
        USD = "USD"

    import bson
    def __init__(self, value:bson.Decimal128, currency_code:CurrencyCode) -> None:
        self.value = value
        self.currency_code = currency_code

    def __getattribute__(self, name):
        if name == '__dict__':
            modified_dict = super().__getattribute__('__dict__').copy()
            modified_dict['currency_code'] = self.currency_code._value_
            return modified_dict
        return super().__getattribute__(name)
