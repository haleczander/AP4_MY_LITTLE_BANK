from DTO import transaction_type
from repo import transaction_type_repo
from .service import Service


class TransactionTypeService( Service ):

    def __init__(self):
        super().__init__()

    #read
    def find_by_id(self, id):
        dbElement = transaction_type_repo.find_by_id(id)
        return transaction_type.TransactionType(dbElement.label)

    def find_all(self):
        dbElements = transaction_type_repo.find_all()
        elementList = []
        for dbElement in dbElements:
            elementList.append(transaction_type.TransactionType(dbElement.label))
        return elementList

