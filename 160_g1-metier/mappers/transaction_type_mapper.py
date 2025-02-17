from dto import TransactionType
from .mapper import Mapper

class TransactionTypeMapper(Mapper):
    def __init__(self):
        pass
    
    def map_to_dto(self, fetched):
        id_transaction_type, label = fetched
        transaction_type = TransactionType()
        transaction_type.set_id_transaction_type(id_transaction_type)
        transaction_type.set_label(label)
        return transaction_type