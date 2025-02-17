from flask import Blueprint, request
import requests
from config import API

transaction_bp = Blueprint('transaction', __name__)

ENDPOINT = f"{API}/transaction"

@transaction_bp.post(f"{ENDPOINT}/card")
def post_transaction_card():
    return requests.post(f"{ENDPOINT}/card", json=request.get_json()) 


@transaction_bp.post(f"{ENDPOINT}/check")
def post_transaction_check():
    return requests.post(f"{ENDPOINT}/check", json=request.get_json())


@transaction_bp.post(f"{ENDPOINT}/transfer")
def post_transaction_transfer():
    return requests.post(f"{ENDPOINT}/transfer", json=request.get_json())
