from repo.account_repo import AccountRepo

# from .transaction_service import TransactionService
from .service import Service


class AccountService(Service):

    def __init__(self):
        super().__init__()
        self.account_repo = AccountRepo()
        # self.transaction_service = TransactionService()

    # create
    def create_account(self, sold, currency):
        if sold >= 0:
            self.account_repo.create_account(sold, currency)
            return 0
        else:
            return -1

    # read
    def is_account_exists(self, id):
        if self.account_repo.find_by_id(id) is None:
            return False
        else:
            return True

    def get_account(self, id):
        account = self.account_repo.find_by_id(id)
        return account

    def get_balance(self, id):
        balance = self.account_repo.get_balance()
        if balance is None:
            return -1
        return balance

    def get_details(self, id):
        details = self.transaction_service.get_transactions_by_account(id)
        if details is None:
            return -1
        return details

    # update
    def update_sold(self, id, sold, currency):
        return self.account_repo.update_sold(id, sold, currency)

    def transfer(self, source_acc, destination_acc, currency, amount):
        # self.transaction_service.create_transaction(source_acc, destination_acc, currency, amount, "transfer")
        return 0
