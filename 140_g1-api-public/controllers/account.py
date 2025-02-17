from flask import Blueprint, request, jsonify
from requests import get, post
from config import API


account_bp = Blueprint('account', __name__)

ENDPOINT = f"{API}/account"

@account_bp.post(ENDPOINT)
def post_account_exists():
    return post(f"{ENDPOINT}", json=request.get_json())
    

ACCOUNT_ENDPOINT = f"{ENDPOINT}/<account>"

@account_bp.get(f"{ACCOUNT_ENDPOINT}/balance")
def get_account_balance(account):
    return get(f"{ENDPOINT}/{account}/balance")
    

@account_bp.get(f"{ACCOUNT_ENDPOINT}/details")
def get_account_details(account):
    return get(f"{ENDPOINT}/{account}/details")


@account_bp.post(f"{ACCOUNT_ENDPOINT}/transfer")
def post_account_transfer(account):
    return post(f"{ENDPOINT}/{account}/transfer", json=request.get_json())
