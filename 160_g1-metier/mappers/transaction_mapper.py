from dto import Transaction
from .mapper import Mapper

class TransactionMapper(Mapper):
    def __init__(self):
        pass
    
    def map_to_dto(self, fetched):
        if not fetched:
            return
        # source_account, dest_account, currency, amount, label, timestamp, type
        transaction = Transaction()
        transaction.set_id_transaction(fetched["transaction_id"])
        transaction.set_source(fetched["source_account"])
        transaction.set_destination(fetched["dest_account"])
        transaction.set_amount(float(fetched["amount"]))
        transaction.set_currency(fetched["currency"])
        transaction.set_label(fetched["label"])
        transaction.set_type(fetched["type"])
        transaction.set_datetime(fetched["timestamp"])
        return transaction