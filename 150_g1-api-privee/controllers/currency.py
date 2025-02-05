from flask import Blueprint, request, jsonify
import requests
from config import CONFIG

currency_bp = Blueprint('currency', __name__)

ENDPOINT = "/currency"
CURRENCY_ENDPOINT = f"{ENDPOINT}/<currency>"

@currency_bp.get(f"{CURRENCY_ENDPOINT}/allowed")
def get_currency_allowed(currency):
    try:
        response = requests.get(f"{CONFIG['API_URL']}/{ENDPOINT}/{currency}/allowed")
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@currency_bp.post(f"{CURRENCY_ENDPOINT}/rate")
def post_currency_rate(currency):
    try:
        data = request.get_json()
        payload = {
            "rate": data.get("rate"),
            "currency": data.get("currency")
        }
        if not payload["rate"] or not payload["currency"]:
            return jsonify({"error": "Les champs 'rate' et 'currency' sont requis."}), 400

        response = requests.post(
            f"{CONFIG['API_URL']}/{ENDPOINT}/{currency}/rate",
            json=payload
        )
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
