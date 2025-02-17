from .repository import Repository
from mappers import CurrencyRateMapper

class CurrencyRateRepo(Repository):
    def __init__(self):
        super().__init__(CurrencyRateMapper())

    def get_currency(self, label):

        return "tbd"
