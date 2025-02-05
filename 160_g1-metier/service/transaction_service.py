from DTO import transaction, account
from repo import transaction_repo

#create
def create_transaction(source_acc, destination_acc, currency, amount, label, datetime, type):
    new_transaction = transaction.Transaction(source_acc, destination_acc, currency, amount, label, datetime, type)
    return transaction_repo.create_transaction(new_transaction)

#read
def find_by_id(id):
    dbElement = transaction_repo.find_by_id(id)
    return transaction.Transaction(dbElement.id, dbElement.source_acc, dbElement.destination_acc, dbElement.currency, dbElement.amount, dbElement.label, dbElement.datetime, dbElement.type)

def find_all():
    dbElements = transaction_repo.find_all()
    elementList = []
    for dbElement in dbElements:
        elementList.append(transaction.Transaction(dbElement.id, dbElement.source_acc, dbElement.destination_acc, dbElement.currency, dbElement.amount, dbElement.label, dbElement.datetime, dbElement.type))
    return elementList

#update
def update_transaction(id, source_acc, destination_acc, currency, amount, label, datetime, type):
    updated_transaction = transaction.Transaction(id, source_acc, destination_acc, currency, amount, label, datetime, type)
    return transaction_repo.update_transaction(updated_transaction)