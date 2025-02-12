from DTO import currency_rate
from repo.currency_rate_repo import CurrencyRateRepo

currency_rate_repo = CurrencyRateRepo()

class CurrencyRateService:

    def getCurrencyRate(currency):
        return currency_rate_repo.getCurrencyRate(currency)