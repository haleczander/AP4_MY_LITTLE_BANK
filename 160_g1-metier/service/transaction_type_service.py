from dto import TransactionType
from repo import TransactionTypeRepo
from .service import Service


class TransactionTypeService(Service):

    def __init__(self):
        super().__init__()
        self.transaction_type_repo = TransactionTypeRepo()

    # read
    def find_by_id(self, id):
        dbElement = self.transaction_type_repo.find_by_id(id)
        return TransactionType(dbElement.label)

    def find_all(self):
        dbElements = self.transaction_type_repo.find_all()
        elementList = []
        for dbElement in dbElements:
            elementList.append(TransactionType(dbElement.label))
        return elementList
