from DTO import transaction, account
from repo import transaction_repo
from service.account_service import AccountService

transaction_repo = transaction_repo.TransactionRepo()
account_service = AccountService()

class TransactionService:

    #create
    def create_transaction(source_acc, destination_acc, currency, amount, label, datetime, type):
        transaction_repo.create_transaction(source_acc, destination_acc, currency, amount, label, datetime, type)
        account_service.update_sold(source_acc, account_service.get_balance(source_acc) - amount, currency)
        account_service.update_sold(destination_acc, account_service.get_balance(destination_acc) + amount, currency)
        return

    #read
    def find_by_id(id):
        transaction = transaction_repo.find_by_id(id)
        return transaction
    def get_transactions_by_account(account_id):
        transactions = transaction_repo.get_by_account(account_id)
        transactionList = []
        for transaction in transactions:
            transactionList.append(transaction.Transaction(transaction.id, transaction.source_acc, transaction.destination_acc, transaction.currency, transaction.amount, transaction.label, transaction.datetime, transaction.type))
        return transactions