from flask import Blueprint
from service.currency_service import CurrencyService
from service.currency_rate_service import CurrencyRateService

currency_bp = Blueprint('currency', __name__)

ENDPOINT = "/currency"
CURRENCY_ENDPOINT = f"{ENDPOINT}/<currency>"

currency_service = CurrencyService()
currency_rate_service = CurrencyRateService()

@currency_bp.get(f"{CURRENCY_ENDPOINT}/allowed")
def get_currency_allowed(currency):
    isAllowed = currency_service.check_currency(currency)
    if isAllowed:
        return f"<p>Currency {currency} is allowed</p>"
    else:
        return f"<p>Currency {currency} is not allowed</p>"

@currency_bp.post(f"{CURRENCY_ENDPOINT}/rate")
def post_currency_rate(currency):
    currency_rate_service.getCurrencyRate(currency)
    return f"<p>Rate for {currency} is 1.23</p>"
