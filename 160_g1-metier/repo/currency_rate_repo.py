from .repository import Repository
from mappers import CurrencyRateMapper

class CurrencyRateRepo(Repository):
    def __init__(self):
        super().__init__(CurrencyRateMapper())

    def set_currency_rate(self, currency, target_currency, rate):
        return "tbd"
