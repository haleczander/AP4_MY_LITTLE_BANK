from dto import Account
from .mapper import Mapper

class AccountMapper(Mapper):
    def __init__(self):
        pass
    
    def map_to_dto(self, fetched):
        account_number, currency, balance = fetched
        account = Account()
        account.set_account_number(account_number)
        account.set_currency(currency)
        account.set_balance(balance)
        return account
        
