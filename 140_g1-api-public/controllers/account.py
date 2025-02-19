from flask import Blueprint, request, jsonify
from requests import get, post
from config import API


account_bp = Blueprint('account', __name__)

ENDPOINT = "/account"

@account_bp.post(ENDPOINT)
def post_account_exists():
    response = post(f"{API}{ENDPOINT}", json=request.get_json())
    return response.content, response.status_code
    

ACCOUNT = "<account>"

@account_bp.get(f"{ENDPOINT}/{ACCOUNT}/balance")
def get_account_balance(account):
    response = get(f"{API}{ENDPOINT}/{account}/balance")
    return response.content, response.status_code
    

@account_bp.get(f"{ENDPOINT}/{ACCOUNT}/details")
def get_account_details(account):
    response = get(f"{API}{ENDPOINT}/{account}/details")
    return response.content, response.status_code


@account_bp.post(f"{ENDPOINT}/{ACCOUNT}/transfer")
def post_account_transfer(account):
    response = post(f"{API}{ENDPOINT}/{account}/transfer", json=request.get_json())
    return response.content, response.status_code
