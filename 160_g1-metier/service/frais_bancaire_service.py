from dto import FraisBancaire
from .service import Service
from repo import FraisBancaireRepo


class FraisBancaireService(Service):

    def __init__(self):
        super().__init__()
        self.frais_bancaire_repo = FraisBancaireRepo()

    # create
    def create_frais_bancaire(self, amount, currency):
        self.frais_bancaire_repo.create(amount, currency)
        return 0

    # read
    def find_by_id(self, id):
        dbElement = self.frais_bancaire_repo.find_by_id(id)
        return FraisBancaire(dbElement.id, dbElement.amount, dbElement.currency)

    def find_all(self):
        dbElements = self.frais_bancaire_repo.find_all()
        elementList = []
        for dbElement in dbElements:
            elementList.append(
                FraisBancaire(dbElement.id, dbElement.amount, dbElement.currency)
            )
        return elementList

    # update
    def update_frais_bancaire(self, id, amount, currency):
        self.frais_bancaire_repo.update(id, amount, currency)
        return 0

    # delete
    def delete_frais_bancaire(self, id):
        self.frais_bancaire_repo.delete(id)
        return 0
