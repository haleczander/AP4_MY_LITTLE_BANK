from flask import Blueprint, request, jsonify
from requests import get, post
from config import API


account_bp = Blueprint('account', __name__)

ENDPOINT = "/account"

@account_bp.post(ENDPOINT)
def post_account_exists():
    return post(f"{API}{ENDPOINT}", json=request.get_json()).account
    

ACCOUNT = "<account>"

@account_bp.get(f"{ENDPOINT}/{ACCOUNT}/balance")
def get_account_balance(account):
    return get(f"{API}{ENDPOINT}/{account}/balance").content
    

@account_bp.get(f"{ENDPOINT}/{ACCOUNT}/details")
def get_account_details(account):
    return get(f"{API}{ENDPOINT}/{account}/details").content


@account_bp.post(f"{ENDPOINT}/{ACCOUNT}/transfer")
def post_account_transfer(account):
    return post(f"{ENDPOINT}/{account}/transfer", json=request.get_json()).content
