from repo.currency_rate_repo import CurrencyRateRepo
from .service import Service


class CurrencyRateService(Service):

    def __init__(self):
        super().__init__()
        self.currency_rate_repo = CurrencyRateRepo()

    def getCurrencyRate(self, currency):
        return self.currency_rate_repo.getCurrencyRate(currency)
