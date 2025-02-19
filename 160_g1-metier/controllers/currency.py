from flask import Blueprint, request
from service.currency_service import CurrencyService
from service.currency_rate_service import CurrencyRateService

currency_bp = Blueprint("currency", __name__)

ENDPOINT = "/currency"
CURRENCY_ENDPOINT = f"{ENDPOINT}/<currency>"

currency_service = CurrencyService()
currency_rate_service = CurrencyRateService()


@currency_bp.get(ENDPOINT)
def get_currencies():
    currencies = currency_service.get_currencies()
    return f"<p>{currencies}</p>"


@currency_bp.get(f"{CURRENCY_ENDPOINT}/allowed")
def get_currency_allowed(currency):
    isAllowed = currency_service.check_currency(currency)
    if isAllowed:
        return f"<p>Currency {currency} is allowed</p>"
    else:
        return f"<p>Currency {currency} is not allowed</p>"


@currency_bp.post(f"{CURRENCY_ENDPOINT}/rate")
def post_currency_rate(currency):
    data = request.get_json()
    if not data or 'rate' not in data or 'currency' not in data:
        return {"message": "Invalid parameters"}, 400

    rate = data['rate']
    target_currency = data['currency']

    try:
        currency_rate_service.set_currency_rate(currency, target_currency, rate)
        return {"message": "Rate has been set successfully"}, 200
    except NotImplementedError:
        return {"message": "Currencies not implemented"}, 501
