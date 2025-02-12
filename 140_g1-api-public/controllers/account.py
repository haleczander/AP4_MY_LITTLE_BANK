from flask import Blueprint, request, jsonify
import requests
from config import CONFIG


account_bp = Blueprint('account', __name__)

ENDPOINT = "/account"
ACCOUNT_ENDPOINT = f"{ENDPOINT}/<account>"

@account_bp.post(ENDPOINT)
def post_account_exists():
    try:
        data = request.get_json()
        response = requests.post(f"{CONFIG['API_URL']}/{ENDPOINT}", json=data)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@account_bp.get(f"{ACCOUNT_ENDPOINT}/balance")
def get_account_balance(account):
    try:
        response = requests.get(f"{CONFIG['API_URL']}/{ENDPOINT}/{account}/balance")
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@account_bp.get(f"{ACCOUNT_ENDPOINT}/details")
def get_account_details(account):
    try:
        response = requests.get(f"{CONFIG['API_URL']}/{ENDPOINT}/{account}/details")
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@account_bp.post(f"{ACCOUNT_ENDPOINT}/transfer")
def post_account_transfer(account):
    try:
        data = request.get_json()
        response = requests.post(f"{CONFIG['API_URL']}/{ENDPOINT}/{account}/transfer", json=data)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
