from flask import Blueprint, json, request, jsonify, abort
from service.account_service import AccountService
from service.currency_service import CurrencyService
from service.transaction_service import TransactionService

account_bp = Blueprint("account", __name__)

ENDPOINT = "/account"
ACCOUNT_ENDPOINT = f"{ENDPOINT}/<account>"

account_service = AccountService()
currency_service = CurrencyService()
transaction_service = TransactionService()


# Account
@account_bp.post(ENDPOINT)
def post_account():
    data = request.get_json()
    payload = {"balance": data.get("balance")}
    
    if not "balance" in data:
        return jsonify({"error": "Le champ 'balance' est requis."}), 400
    
    try:
        account = account_service.create_account( payload["balance"], 'EUR' )
        if account is None:
            return jsonify({"error": "Erreur lors de la création du compte"}), 500
        return jsonify(account_service.json(account)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400




@account_bp.get(f"{ACCOUNT_ENDPOINT}/exists")
def get_account_exists(account):
    acc = account_service.get_account(account)
    return jsonify(not not acc), 200 if acc else 404


@account_bp.get(f"{ACCOUNT_ENDPOINT}/balance")
def get_account_balance(account):
    
    account = account_service.get_account(account)
    if not account :
        return jsonify({"error": "Compte introuvable"}), 404
    return jsonify(account_service.json(account)), 200


@account_bp.get(f"{ACCOUNT_ENDPOINT}/details")
def get_account_details(account):
    details = transaction_service.get_transactions_by_account(account)
    details = [ transaction_service.json_detail(detail) for detail in details ]
    account = account_service.get_account(account)
    if not account:
        return jsonify({"error": "Compte introuvable"}), 404
    account = account_service.json(account)
    account.setdefault("operations", details)
    return jsonify(account), 200

@account_bp.post(f"{ACCOUNT_ENDPOINT}/transfer")
def get_account_transfer(account):
    data = request.get_json()
    payload = {
        "amount": data.get("amount"),
        "currency": data.get("currency"),
        "label": data.get("label"),
        "recipient": data.get("recipient")
    }

    if (
        not payload["amount"]
        or not payload["currency"]
        or not payload["label"]
        or not payload["recipient"]
    ):
        return (
            jsonify(
                {
                    "error": "Les champs 'source_acc', 'destination_acc', 'currency' et 'amount' sont requis."
                }
            ),
            400,
        )

    if not account_service.get_account(account):
        return jsonify({"error": "Compte source introuvable"}), 404
    
    transaction = transaction_service.create_transaction(
        account, payload["recipient"], payload["currency"], payload["amount"], "now()", payload["label"], "TRANSFER"
    )
    
    if not transaction:
        return jsonify({"error": "Erreur lors de la transaction"}), 500
    return jsonify(transaction_service.json_transfer(transaction)), 200