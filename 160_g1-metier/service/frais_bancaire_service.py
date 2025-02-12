from DTO import frais_bancaire
from repo import frais_bancaire_repo
from service import Service


class FraisBancaireService( Service ):
    
    def __init__(self):
        super().__init__()

    #create
    def create_frais_bancaire(self, amount, currency):
        dbElement = frais_bancaire_repo.create(amount, currency)
        return 0

    #read
    def find_by_id(self, id):
        dbElement = frais_bancaire_repo.find_by_id(id)
        return frais_bancaire.FraisBancaire(dbElement.id, dbElement.amount, dbElement.currency)

    def find_all(self):
        dbElements = frais_bancaire_repo.find_all()
        elementList = []
        for dbElement in dbElements:
            elementList.append(frais_bancaire.FraisBancaire(dbElement.id, dbElement.amount, dbElement.currency))
        return elementList

    #update
    def update_frais_bancaire(self, id, amount, currency):
        frais_bancaire_repo.update(id, amount, currency)
        return 0

    #delete
    def delete_frais_bancaire(self, id):
        frais_bancaire_repo.delete(id)
        return 0