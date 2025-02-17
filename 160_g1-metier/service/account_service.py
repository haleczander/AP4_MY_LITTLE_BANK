from repo import AccountRepo
from exceptions import NotEnoughMoneyException

# from .transaction_service import TransactionService
from .service import Service


class AccountService(Service):

    def __init__(self):
        super().__init__()
        self.account_repo = AccountRepo()
        # self.transaction_service = TransactionService()

    # create
    def create_account(self, balance, currency):
        if balance < 0 :
            raise NotEnoughMoneyException()
        return self.account_repo.create_account(balance, currency)

    # read
    def is_account_exists(self, id):
        return not not self.get_account(id)

    def get_account(self, id):
        account = self.account_repo.find_by_id(id)
        return account

    def get_balance(self, id):
        return self.account_repo.get_balance()

    def get_details(self, id):
        return self.transaction_service.get_transactions_by_account(id)
        
    # update
    def update_balance(self, id, balance, currency):
        return self.account_repo.update_balance(id, balance, currency)

    def transfer(self, source_acc, destination_acc, currency, amount):
        # self.transaction_service.create_transaction(source_acc, destination_acc, currency, amount, "transfer")
        return 0
