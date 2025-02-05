from flask import Blueprint, jsonify
import requests
from config import CONFIG

account_bp = Blueprint('account', __name__)

ENDPOINT = "/account"
ACCOUNT_ENDPOINT = f"{ENDPOINT}/<account>"

@account_bp.get(f"{ACCOUNT_ENDPOINT}/exists")
def get_account_exists(account):
    try:
        response = requests.get(f"{CONFIG['API_URL']}/{ENDPOINT}/{account}/exists")
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
