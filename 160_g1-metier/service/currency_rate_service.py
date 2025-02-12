from DTO import currency_rate
from repo.currency_rate_repo import CurrencyRateRepo
from service import Service

currency_rate_repo = CurrencyRateRepo()

class CurrencyRateService( Service ):
    
    def __init__(self):
        super().__init__()

    def getCurrencyRate(self, currency):
        return currency_rate_repo.getCurrencyRate(currency)