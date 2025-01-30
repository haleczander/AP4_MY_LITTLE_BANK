from flask import Blueprint

transaction_bp = Blueprint('transaction', __name__)

ENDPOINT = "/transaction"

@transaction_bp.post(f"{ENDPOINT}/card")
def transaction_card():
    # Logique pour une transaction avec carte
    return "<p>Transaction with card</p>"

@transaction_bp.post(f"{ENDPOINT}/check")
def transaction_check():
    # Logique pour une transaction par chèque
    return "<p>Transaction with check</p>"

@transaction_bp.post(f"{ENDPOINT}/transfer")
def transaction_transfer():
    # Logique pour un virement
    return "<p>Transaction with transfer</p>"
