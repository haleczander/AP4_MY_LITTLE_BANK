from repo import TransactionRepo
from dto import Transaction
from .service import Service


class TransactionService(Service):

    def __init__(self):
        super().__init__()
        self.transaction_repo = TransactionRepo()

    # create
    def create_transaction(
        self, source_acc, destination_acc, currency, amount, datetime, label, type
    ):
        return self.transaction_repo.execute_transaction(
            source_acc, destination_acc, currency, amount, label, datetime, type
        )

    # read
    def find_by_id(self, id):
        transaction = self.transaction_repo.find_by_id(id)
        return transaction

    def get_transactions_by_account(self, account_id):
        return self.transaction_repo.get_by_account(account_id)
    
    def json_transfer( self, transaction):
        if not transaction: return transaction
        return {
            "amount": transaction.amount,
            "currency": transaction.currency,
            "label": transaction.label,
            "recipient": transaction.destination
        }
        
    def json_detail(self, transaction):
        return {
            "timestamp": transaction.datetime,
            "label": transaction.label,
            "amount": transaction.amount
        }

        
