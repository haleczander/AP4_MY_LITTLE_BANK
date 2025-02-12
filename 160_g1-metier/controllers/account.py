from flask import Blueprint, request, jsonify
from service.account_service import AccountService
from service.transaction_service import TransactionService

account_bp = Blueprint('account', __name__)

ENDPOINT = "/account"
ACCOUNT_ENDPOINT = f"{ENDPOINT}/<account>"

account_service = AccountService()
transaction_service = TransactionService()

# Account
@account_bp.post(ENDPOINT)
def post_account():
    return "<p>Account exists</p>"

@account_bp.get(f"{ACCOUNT_ENDPOINT}/exists")
def get_account_exists(account):
    # Logique pour vérifier l'existence du compte
    account = account_service.get_account(account)
    return jsonify(not not account)
 

@account_bp.get(f"{ACCOUNT_ENDPOINT}/balance")
def get_account_balance(account):
    balance = account_service.get_balance(account)
    return jsonify(balance)

@account_bp.get(f"{ACCOUNT_ENDPOINT}/details")
def get_account_details(account):
    details = account_service.get_details(account)
    return jsonify(details)

@account_bp.post(f"{ACCOUNT_ENDPOINT}/transfer")
def get_account_transfer(account):
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
    
    account_service.transfer(payload["source_acc"], payload["destination_acc"], payload["currency"], payload["amount"])
    return f"<p>Transfer from account {account}</p>"