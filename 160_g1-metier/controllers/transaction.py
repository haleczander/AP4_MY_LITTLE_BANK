from flask import Blueprint, request, jsonify
from service.transaction_service import TransactionService
from service.account_service import AccountService

transaction_bp = Blueprint('transaction', __name__)

ENDPOINT = "/transaction"

transaction_service = TransactionService()
account_service = AccountService()

@transaction_bp.post(f"{ENDPOINT}/card")
def post_transaction_card():
    data = request.get_json()
    payload = {
        "source_acc": data.get("source_acc"),
        "destination_acc": data.get("destination_acc"),
        "currency": data.get("currency"),
        "amount": data.get("amount"),
        "label": data.get("label"),
        "datetime": data.get("datetime")
    }
    if not payload["source_acc"] or not payload["destination_acc"] or not payload["currency"] or not payload["amount"]:
        return jsonify({"error": "Les champs 'source_acc', 'destination_acc', 'currency' et 'amount' sont requis."}), 400
    
    transaction_service.create_transaction(payload["source_acc"], payload["destination_acc"], payload["currency"], payload["amount"], payload["label"], payload["datetime"], "card")
    
    return "<p>Transaction with card done </p>"

@transaction_bp.post(f"{ENDPOINT}/check")
def post_transaction_check():
    data = request.get_json()
    payload = {
        "source_acc": data.get("source_acc"),
        "destination_acc": data.get("destination_acc"),
        "currency": data.get("currency"),
        "amount": data.get("amount"),
        "label": data.get("label"),
        "datetime": data.get("datetime")
    }
    if not payload["source_acc"] or not payload["destination_acc"] or not payload["currency"] or not payload["amount"]:
        return jsonify({"error": "Les champs 'source_acc', 'destination_acc', 'currency' et 'amount' sont requis."}), 400
    
    transaction_service.create_transaction(payload["source_acc"], payload["destination_acc"], payload["currency"], payload["amount"], payload["label"], payload["datetime"], "check")
    
    return "<p>Transaction with check</p>"

@transaction_bp.post(f"{ENDPOINT}/transfer")
def post_transaction_transfer():
    data = request.get_json()
    payload = {
        "source_acc": data.get("source_acc"),
        "destination_acc": data.get("destination_acc"),
        "currency": data.get("currency"),
        "amount": data.get("amount"),
        "label": data.get("label"),
        "datetime": data.get("datetime")
    }
    if not payload["source_acc"] or not payload["destination_acc"] or not payload["currency"] or not payload["amount"]:
        return jsonify({"error": "Les champs 'source_acc', 'destination_acc', 'currency' et 'amount' sont requis."}), 400
    
    transaction_service.create_transaction(payload["source_acc"], payload["destination_acc"], payload["currency"], payload["amount"], payload["label"], payload["datetime"], "transfer")
    
    return "<p>Transaction with transfer</p>"
