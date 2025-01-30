from flask import Blueprint

currency_bp = Blueprint('currency', __name__)

ENDPOINT = "/currency"
CURRENCY_ENDPOINT = f"{ENDPOINT}/<currency>"

@currency_bp.get(f"{CURRENCY_ENDPOINT}/allowed")
def currency_allowed(currency):
    # Logique pour vérifier la devise
    return f"<p>Currency {currency} is allowed</p>"

@currency_bp.post(f"{CURRENCY_ENDPOINT}/rate")
def currency_rate(currency):
    # Logique pour retourner le taux
    return f"<p>Rate for {currency} is 1.23</p>"
