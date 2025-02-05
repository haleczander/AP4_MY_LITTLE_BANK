from flask import Blueprint
import requests
from config import CONFIG

transaction_bp = Blueprint('transaction', __name__)

ENDPOINT = "/transaction"

@transaction_bp.post(f"{ENDPOINT}/card")
def post_transaction_card():
    try:
        response = requests.post(f"{CONFIG['API_URL']}/{ENDPOINT}/card")
        return response
    except requests.exceptions.RequestException as e:
        return e

@transaction_bp.post(f"{ENDPOINT}/check")
def post_transaction_check():
    try:
        response = requests.post(f"{CONFIG['API_URL']}/{ENDPOINT}/check")
        return response
    except requests.exceptions.RequestException as e:
        return e

@transaction_bp.post(f"{ENDPOINT}/transfer")
def post_transaction_transfer():
    # Logique pour un virement
    return "<p>Transaction with transfer</p>"
