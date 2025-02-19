from flask import Blueprint, jsonify, request
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
    return jsonify(currencies),200


@currency_bp.get(f"{CURRENCY_ENDPOINT}/allowed")
def get_currency_allowed(currency):
    isAllowed = currency_service.check_currency(currency)
    if isAllowed:
        return f"La devise est acceptée.", 200
    else:
        return f"La devise n'est pas acceptées.", 400


@currency_bp.post(f"{CURRENCY_ENDPOINT}/rate")
def post_currency_rate(currency):
    data = request.get_json()
    if not data or 'rate' not in data or 'currency' not in data:
        return {"message": "Invalid parameters"}, 400

    rate = data['rate']
    target_currency = data['currency']
    try:
        currency_rate = currency_rate_service.set_currency_rate(currency, target_currency, rate)
        return (jsonify(currency_rate), 200)
    except Exception as e:
        return {"message": str(e)}, 400