from flask import Blueprint, jsonify
import requests
from config import API

account_bp = Blueprint('account', __name__)

ENDPOINT = "/account"
ACCOUNT = "<account>"

@account_bp.get(f"{ENDPOINT}/{ACCOUNT}/exists")
def get_account_exists(account):
    response = requests.get(f"{API}{ENDPOINT}/{account}/exists")
    return response.content, response.status_code

