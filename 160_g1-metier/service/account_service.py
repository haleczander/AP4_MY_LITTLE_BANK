from repo.account_repo import AccountRepo
import transaction_service
from service import Service


account_repo = AccountRepo()
transaction_service = transaction_service.TransactionService()


class AccountService( Service ):

    def __init__(self):
        super().__init__()


    #create
    def create_account(self, id, sold, currency):
        dbElement = account_repo.create_account(id, sold, currency)
        return 0

    #read
    def get_account(self, id):
        account_exist = account_repo.find_by_id(id)
        return account_exist

    def get_balance(self, id):
        balance = account_repo.get_balance()
        return balance

    def get_details(self, id):
        details = transaction_service.get_transactions_by_account(id)
        return details

    #update
    def update_sold(self, id, sold, currency):
        return account_repo.update_sold(id, sold, currency)
        
    def transfer(self, source_acc, destination_acc, currency, amount):
        transaction_service.create_transaction(source_acc, destination_acc, currency, amount, "transfer")
        return 0

