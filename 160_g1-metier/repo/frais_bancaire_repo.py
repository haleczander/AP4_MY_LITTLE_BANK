from .repository import Repository
from mappers import FraisBancaireMapper

class FraisBancaireRepo(Repository):
    def __init__(self):
        super().__init__(FraisBancaireMapper())
