from flask import Blueprint, request, jsonify, abort
from service.account_service import AccountService
from service.currency_service import CurrencyService

account_bp = Blueprint("account", __name__)

ENDPOINT = "/account"
ACCOUNT_ENDPOINT = f"{ENDPOINT}/<account>"

account_service = AccountService()
currency_service = CurrencyService()


# Account
@account_bp.post(ENDPOINT)
def post_account():
    data = request.get_json()
    payload = {"balance": data.get("balance")}
    
    if not "balance" in data:
        return jsonify({"error": "Le champ 'balance' est requis."}), 400
    
    try:
        account = account_service.create_account( payload["balance"] )
        if account is None:
            return jsonify({"error": "Erreur lors de la création du compte"}), 500
        return jsonify({"message": "Compte créé", "account": account}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400




@account_bp.get(f"{ACCOUNT_ENDPOINT}/exists")
def get_account_exists(account):
    if not isinstance(account, int):
        abort(400, "Identifiant invalide")
    if not account_service.is_account_exists(account):
        abort(404, "Compte introuvable")
    else:
        return f"<p>Account {account} exists</p>"


@account_bp.get(f"{ACCOUNT_ENDPOINT}/balance")
def get_account_balance(account):
    balance = account_service.get_balance(account)
    if balance == 0:
        return f"<p>Balance : {balance}</p>"
    elif balance == -1:
        abort(404, "Can't find balance")
    else:
        abort(500)


@account_bp.get(f"{ACCOUNT_ENDPOINT}/details")
def get_account_details(account):
    details = account_service.get_details(account)
    if details == 0:
        return f"<p>Details : {details}</p>"
    else:
        abort(404, "Can't find details")


@account_bp.post(f"{ACCOUNT_ENDPOINT}/transfer")
def get_account_transfer(account):
    data = request.get_json()
    payload = {
        "source_acc": data.get("source_acc"),
        "destination_acc": data.get("destination_acc"),
        "currency": data.get("currency"),
        "amount": data.get("amount"),
        "label": data.get("label"),
        "datetime": data.get("datetime"),
    }

    # Check required fields
    if (
        not payload["source_acc"]
        or not payload["destination_acc"]
        or not payload["currency"]
        or not payload["amount"]
    ):
        return (
            jsonify(
                {
                    "error": "Les champs 'source_acc', 'destination_acc', 'currency' et 'amount' sont requis."
                }
            ),
            400,
        )

    # Validate destination account
    if not isinstance(payload["destination_acc"], int):
        return jsonify({"error": "Identifiant invalide"}), 400
    if not account_service.is_account_exists(payload["destination_acc"]):
        return jsonify({"error": "Compte destination introuvable"}), 400

    # Validate label
    if not payload["label"]:
        return jsonify({"error": "Libellé requis"}), 400

    # Check if source account has enough balance
    source_balance = account_service.get_balance(payload["source_acc"])
    if source_balance < payload["amount"]:
        return jsonify({"error": "balancee insuffisant"}), 400

    # Check if currencies match
    source_currency = account_service.get_currency(payload["source_acc"])
    destination_currency = account_service.get_currency(payload["destination_acc"])
    if source_currency != destination_currency:
        # Perform currency conversion if needed
        converted_amount = currency_service.convert_currency(
            payload["amount"], source_currency, destination_currency
        )
        if converted_amount is None:
            return jsonify({"error": "Erreur de conversion de devise"}), 400
        payload["amount"] = converted_amount

    # Debit source account
    if not account_service.debit_account(payload["source_acc"], payload["amount"]):
        return jsonify({"error": "Erreur lors du débit du compte source"}), 500

    # Credit destination account
    if not account_service.credit_account(
        payload["destination_acc"], payload["amount"]
    ):
        return jsonify({"error": "Erreur lors du crédit du compte destination"}), 500

    # Update transaction in database
    transaction_id = account_service.create_transaction(payload)
    if transaction_id is None:
        return jsonify({"error": "Erreur lors de la création de la transaction"}), 500

    return (
        jsonify({"message": "Virement réussi", "transaction_id": transaction_id}),
        200,
    )
