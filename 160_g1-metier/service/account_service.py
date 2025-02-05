from DTO import account
from repo import account_repo




#create
def create_account(id, sold, currency):
    dbElement = account_repo.create_account(id, sold, currency)
    return 0

#read
def find_by_id(id):
    dbElement = account_repo.find_by_id(id)
    return account.Account(dbElement.id, dbElement.sold, dbElement.currency)

def find_all():
    dbElements = account_repo.find_all()
    elementList = []
    for dbElement in dbElements:
        elementList.append(account.Account(dbElement.id, dbElement.sold, dbElement.currency))
    return elementList

#update
def update_account(id, sold, currency):
    dbElement = account_repo.update_account(id, sold, currency)
    return 0

#delete
def delete_account(id):
    account_repo.delete_account(id)
    return 0



