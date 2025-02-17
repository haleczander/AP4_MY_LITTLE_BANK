from flask import Blueprint, request
import requests
from config import API

currency_bp = Blueprint('currency', __name__)

ENDPOINT = f"{API}/currency"
CURRENCY_ENDPOINT = f"{ENDPOINT}/<currency>"

@currency_bp.get(f"{CURRENCY_ENDPOINT}/allowed")
def get_currency_allowed(currency):
    return requests.get(f"{ENDPOINT}/{currency}/allowed")


@currency_bp.post(f"{CURRENCY_ENDPOINT}/rate")
def post_currency_rate(currency):
    return requests.post(f"{ENDPOINT}/{currency}/rate", json=request.get_json())

