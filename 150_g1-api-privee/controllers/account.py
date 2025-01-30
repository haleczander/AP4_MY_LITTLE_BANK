from flask import Blueprint

account_bp = Blueprint('account', __name__)

ENDPOINT = "/account"
ACCOUNT_ENDPOINT = f"{ENDPOINT}/<account>"

@account_bp.get(f"{ACCOUNT_ENDPOINT}/exists")
def account_exists(account):
    # Logique pour vérifier l'existence du compte
    return f"<p>Account {account} exists</p>"