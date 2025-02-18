from flask import Blueprint, request
import requests
from config import API

transaction_bp = Blueprint('transaction', __name__)

ENDPOINT = "/transaction"

@transaction_bp.post(f"{ENDPOINT}/card")
def post_transaction_card():
    return requests.post(f"{API}{ENDPOINT}/card", json=request.get_json()).content


@transaction_bp.post(f"{ENDPOINT}/check")
def post_transaction_check():
    return requests.post(f"{API}{ENDPOINT}/check", json=request.get_json()).content


@transaction_bp.post(f"{ENDPOINT}/transfer")
def post_transaction_transfer():
    return requests.post(f"{API}{ENDPOINT}/transfer", json=request.get_json()).content
