from DTO import currency_rate
from repo import currency_rate_repo



#create
def create_currency_rate(currencyA, currencyB, rate):
    dbElement = currency_rate_repo.create_currency_rate(currencyA, currencyB, rate)
    return 0

#read
def find_by_id(id):
    dbElement = currency_rate_repo.find_by_id(id)
    return currency_rate.CurrencyRate(dbElement.id, dbElement.currencyA, dbElement.currencyB, dbElement.rate)

def find_all():
    dbElements = currency_rate_repo.find_all()
    elementList = []
    for dbElement in dbElements:
        elementList.append(currency_rate.CurrencyRate(dbElement.id, dbElement.currencyA, dbElement.currencyB, dbElement.rate))
    return elementList

#update
def update_currency_rate(id, rate, currencyA, currencyB):
    dbElement = currency_rate_repo.update_currency_rate(id, currencyA, currencyB, rate)
    return 0

#delete
def delete_currency_rate(id):
    currency_rate_repo.delete_currency_rate(id)
    return 0