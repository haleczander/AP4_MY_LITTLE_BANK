from dto import Currency
from .mapper import Mapper


class CurrencyMapper(Mapper):
    def map_to_dto(self, fetched):
        if not fetched:
            return
        currency = Currency()
        currency.set_code( fetched[0] )
        return currency
