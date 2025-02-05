from flask import Blueprint

account_bp = Blueprint('account', __name__)

ENDPOINT = "/account"
ACCOUNT_ENDPOINT = f"{ENDPOINT}/<account>"

# Account
@account_bp.post(ENDPOINT)
def post_account_exists():
    return "<p>Account exists</p>"

@account_bp.get(f"{ACCOUNT_ENDPOINT}/balance")
def get_account_balance(account):
    return f"<p>Account {account} balance is 1000</p>"

@account_bp.get(f"{ACCOUNT_ENDPOINT}/details")
def get_account_details(account):
    return f"<p>Account {account} details</p>"

@account_bp.post(f"{ACCOUNT_ENDPOINT}/transfer")
def post_account_transfer(account):
    return f"<p>Transfer from account {account}</p>"