from flask import Blueprint, request
import requests
from config import API

currency_bp = Blueprint('currency', __name__)

ENDPOINT = "/currency"
CURRENCY = "<currency>"

@currency_bp.get(f"{ENDPOINT}/{CURRENCY}/allowed")
def get_currency_allowed(currency):
    response = requests.get(f"{API}{ENDPOINT}/{currency}/allowed")
    return response.content, response.status_code


@currency_bp.post(f"{ENDPOINT}/{CURRENCY}/rate")
def post_currency_rate(currency):
    response = requests.post(f"{API}{ENDPOINT}/{currency}/rate", json=request.get_json())
    return response.content, response.status_code

