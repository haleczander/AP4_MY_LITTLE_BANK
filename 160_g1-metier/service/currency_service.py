from DTO import currency
from repo.currency_repo import CurrencyRepo
from service import Service

currency_repo = CurrencyRepo()

class CurrencyService( Service ):
    
    def __init__(self):
        super().__init__()

    def check_currency(self, label):
        currency = currency_repo.get_currency(label)
        if currency != None:
            return True
        else:
            return False
        