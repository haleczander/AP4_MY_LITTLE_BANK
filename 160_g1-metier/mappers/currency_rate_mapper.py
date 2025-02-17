from dto import CurrencyRate
from .mapper import Mapper

class CurrencyRateMapper(Mapper):
    def __init__(self):
        pass
    
    def map_to_dto(self, fetched):
        ref_currency, other_currency, rate = fetched
        currency_rate = CurrencyRate()
        currency_rate.set_ref_currency(ref_currency)
        currency_rate.set_other_currency(other_currency)
        currency_rate.set_rate(rate)
        return currency_rate