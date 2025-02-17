from dto import Currency
from .mapper import Mapper


class CurrencyMapper(Mapper):
    def map_to_dto(self, fetched):
        currency = Currency()
        currency.set_code( fetched[0] )
        return currency
