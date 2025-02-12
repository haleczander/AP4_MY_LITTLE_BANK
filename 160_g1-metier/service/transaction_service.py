from DTO import transaction, account
from repo.transaction_repo import TransactionRepo
from service.account_service import AccountService
from .service import Service



class TransactionService( Service ):
    
    def __init__(self):
        super().__init__()
        self.transaction_repo = TransactionRepo()
        self.account_service = AccountService()

    #create
    def create_transaction(self, source_acc, destination_acc, currency, amount, label, datetime, type):
        self.transaction_repo.create_transaction(source_acc, destination_acc, currency, amount, label, datetime, type)
        self.account_service.update_sold(source_acc, self.account_service.get_balance(source_acc) - amount, currency)
        self.account_service.update_sold(destination_acc, self.account_service.get_balance(destination_acc) + amount, currency)
        return

    #read
    def find_by_id(self, id):
        transaction = self.transaction_repo.find_by_id(id)
        return transaction
    def get_transactions_by_account(self, account_id):
        transactions = self.transaction_repo.get_by_account(account_id)
        transactionList = []
        for transaction in transactions:
            transactionList.append(transaction.Transaction(transaction.id, transaction.source_acc, transaction.destination_acc, transaction.currency, transaction.amount, transaction.label, transaction.datetime, transaction.type))
        return transactions