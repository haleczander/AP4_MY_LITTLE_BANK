from DTO import transaction_type
from repo import transaction_type_repo



#create






#read
def find_by_id(id):
    dbElement = transaction_type_repo.find_by_id(id)
    return transaction_type.TransactionType(dbElement.label)

def find_all():
    dbElements = transaction_type_repo.find_all()
    elementList = []
    for dbElement in dbElements:
        elementList.append(transaction_type.TransactionType(dbElement.label))
    return elementList

