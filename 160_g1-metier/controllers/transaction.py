from flask import Blueprint, request, jsonify
from service.transaction_service import TransactionService
from service.account_service import AccountService
import datetime

transaction_bp = Blueprint("transaction", __name__)

ENDPOINT = "/transaction"

transaction_service = TransactionService()
account_service = AccountService()


@transaction_bp.post(f"{ENDPOINT}/card")
def post_transaction_card():
    data = request.get_json()
    payload = {
        "sourceAccount": data.get("sourceAccount"),
        "destAccount": data.get("destAccount"),
        "currency": data.get("currency"),
        "amount": data.get("amount"),
        "merchant": data.get("merchant"),
        "datetime": data.get("datetime"),
    }
    if (
        not payload["sourceAccount"]
        or not payload["destAccount"]
        or not payload["currency"]
        or not payload["amount"]
        or not payload["merchant"]
    ):
        return (
            jsonify(
                {
                    "error": "Les champs 'sourceAccount', 'destAccount', 'currency', 'amount' et 'merchant' sont requis."
                }
            ),
            400,
        )


    transaction_service.create_transaction(
        payload["sourceAccount"],
        payload["destAccount"],
        payload["currency"],
        payload["amount"],
        datetime.datetime.now(),
        payload["label"],
        "card",
    )

    return "<p>Transaction with card done </p>"


@transaction_bp.post(f"{ENDPOINT}/check")
def post_transaction_check():
    data = request.get_json()
    payload = {
        "sourceAccount": data.get("sourceAccount"),
        "destAccount": data.get("destAccount"),
        "currency": data.get("currency"),
        "amount": data.get("amount"),
        "datetime": data.get("datetime"),
    }
    if (
        not payload["sourceAccount"]
        or not payload["destAccount"]
        or not payload["currency"]
        or not payload["amount"]
    ):
        return (
            jsonify(
                {
                    "error": "Les champs 'sourceAccount', 'destAccount', 'currency' et 'amount' sont requis."
                }
            ),
            400,
        )

    transaction = transaction_service.create_transaction(
        payload["sourceAccount"],
        payload["destAccount"],
        payload["currency"],
        payload["amount"],
        datetime.datetime.now(),
        "",
        "check"
    )

    return jsonify({"message": "Transaction with check done", "transaction": transaction}), 200


@transaction_bp.post(f"{ENDPOINT}/transfer")
def post_transaction_transfer():
    data = request.get_json()
    payload = {
        "sourceAccount": data.get("sourceAccount"),
        "destAccount": data.get("destAccount"),
        "currency": data.get("currency"),
        "amount": data.get("amount"),
        "label": data.get("label"),
    }
    if (
        not payload["sourceAccount"]
        or not payload["destAccount"]
        or not payload["currency"]
        or not payload["amount"]
    ):
        return (
            jsonify(
                {
                    "error": "Les champs 'sourceAccount', 'destAccount', 'currency' et 'amount' sont requis."
                }
            ),
            400,
        )

    transaction = transaction_service.create_transaction(
        payload["sourceAccount"],
        payload["destAccount"],
        payload["currency"],
        payload["amount"],
        datetime.datetime.now(),
        payload["label"],
        "transfer",
    )

    return jsonify({"message": "Transaction with transfer done", "transaction": transaction}), 200
