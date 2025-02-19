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
            source_acc, destination_acc, currency, amount, datetime, label, type
        )

    # read
    def find_by_id(self, id):
        transaction = self.transaction_repo.find_by_id(id)
        return transaction

    def get_transactions_by_account(self, account_id):
        transactions = self.transaction_repo.get_by_account(account_id)
        transactionList = []
        for transaction in transactions:
            transactionList.append(
                Transaction(
                    transaction.id,
                    transaction.source_acc,
                    transaction.destination_acc,
                    transaction.currency,
                    transaction.amount,
                    transaction.label,
                    transaction.datetime,
                    transaction.type,
                )
            )
        return transactions
