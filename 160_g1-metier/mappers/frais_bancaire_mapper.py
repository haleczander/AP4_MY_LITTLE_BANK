from dto import FraisBancaire
from .mapper import Mapper

class FraisBancaireMapper(Mapper):
    def __init__(self):
        pass
    
    def map_to_dto(self, fetched):
        id_frais, type_frais, montant = fetched
        frais_bancaire = FraisBancaire()
        frais_bancaire.set_id_frais(id_frais)
        frais_bancaire.set_type_frais(type_frais)
        frais_bancaire.set_montant(montant)
        return frais_bancaire