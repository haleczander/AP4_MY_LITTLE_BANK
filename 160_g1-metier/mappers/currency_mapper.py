from dto import Currency


class CurrencyMapper:
    def map(self, fetched):
        currency = Currency()
        currency.code = fetched[0]
        return currency
