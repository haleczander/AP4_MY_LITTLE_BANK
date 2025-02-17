from flask import Blueprint, jsonify
import requests
from config import API

account_bp = Blueprint('account', __name__)

ENDPOINT = f"{API}/account"
ACCOUNT_ENDPOINT = f"{ENDPOINT}/<account>"

@account_bp.get(f"{ACCOUNT_ENDPOINT}/exists")
def get_account_exists(account):
    return requests.get(f"{ENDPOINT}/{account}/exists")

