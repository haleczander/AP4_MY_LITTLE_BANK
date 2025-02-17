from repo import CurrencyRepo
from .service import Service


class CurrencyService(Service):

    def __init__(self):
        super().__init__()
        self.currency_repo = CurrencyRepo()

    def get_currencies(self):
        currencies = self.currency_repo.get_currencies()
        return currencies

    def check_currency(self, label):
        currency = self.currency_repo.get_currency(label)
        if currency != None:
            return True
        else:
            return False
