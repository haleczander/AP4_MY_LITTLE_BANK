from dto import Transaction
from .mapper import Mapper

class TransactionMapper(Mapper):
    def __init__(self):
        pass
    
    def map_to_dto(self, fetched):
        id_transaction, account_number, amount, transaction_date, transaction_type = fetched
        transaction = Transaction()
        transaction.set_id_transaction(id_transaction)
        transaction.set_account_number(account_number)
        transaction.set_amount(amount)
        transaction.set_transaction_date(transaction_date)
        transaction.set_transaction_type(transaction_type)
        return transaction