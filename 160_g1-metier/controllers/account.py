from flask import Blueprint, request, jsonify, abort
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
        return jsonify({"message": "Compte créé", "account": account}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400




@account_bp.get(f"{ACCOUNT_ENDPOINT}/exists")
def get_account_exists(account):
    acc = account_service.get_account(account)
    return jsonify(not not acc)


@account_bp.get(f"{ACCOUNT_ENDPOINT}/balance")
def get_account_balance(account):
    
    balance = account_service.get_balance(account)
    if not balance :
        return jsonify({"error": "Compte introuvable"}), 404
    return jsonify(balance)


@account_bp.get(f"{ACCOUNT_ENDPOINT}/details")
def get_account_details(account):
    details = transaction_service.get_transactions_by_account(account)
    if details == 0:
        return f"<p>Details : {details}</p>"
    else:
        abort(404, "Can't find details")


@account_bp.post(f"{ACCOUNT_ENDPOINT}/transfer")
def get_account_transfer(account):
    data = request.get_json()
    payload = {
        "amount": data.get("amount"),
        "currency": data.get("currency"),
        "label": data.get("label"),
        "recipient": data.get("recipient")
    }

    # Check required fields
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
    
    transaction_service.create_transaction(
        account, payload["recipient"], payload["currency"], payload["amount"], "now()", payload["label"], "TRANSFER"
    )