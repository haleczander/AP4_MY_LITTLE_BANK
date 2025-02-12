from DTO import currency
from repo.currency_repo import CurrencyRepo

currency_repo = CurrencyRepo()

class CurrencyService:

    def check_currency(label):
        currency = currency_repo.get_currency(label)
        if currency != None:
            return True
        else:
            return False
        