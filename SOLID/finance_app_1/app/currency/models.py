class Currency:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class CurrencyRate:
    def __init__(self, id, from_currency: Currency, to_currency: Currency, rate):
        self.id = id
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.rate = rate
