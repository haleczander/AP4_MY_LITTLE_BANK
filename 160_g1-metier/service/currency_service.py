from DTO import currency
from repo import currency_repo

#create
def create_currency(label, allowed):
    dbElement = currency_repo.create_currency(label, allowed)
    return 0

#read
def find_by_id(id):
    dbElement = currency_repo.find_by_id(id)
    return currency.Currency(dbElement.id, dbElement.label, dbElement.allowed)

def find_all():
    dbElements = currency_repo.find_all()
    elementList = []
    for dbElement in dbElements:
        elementList.append(currency.Currency(dbElement.id, dbElement.label, dbElement.allowed))
    return elementList

#update
def update_currency(id, label, allowed):
    dbElement = currency_repo.update_currency(id, label, allowed)
    return 0

#delete
def delete_currency(id):
    currency_repo.delete_currency(id)
    return 0