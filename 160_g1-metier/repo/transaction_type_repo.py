from .repository import Repository
from mappers import TransactionTypeMapper

class TransactionTypeRepo(Repository):
    def __init__(self):
        super().__init__(TransactionTypeMapper())
