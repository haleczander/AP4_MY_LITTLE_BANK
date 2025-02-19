from dto import Account
from .mapper import Mapper

class AccountMapper(Mapper):
    def __init__(self):
        pass
    
    def map_to_dto(self, fetched):
        if not fetched:
            return
        account_number, balance, currency = fetched["account_number"], fetched["balance"], fetched["currency"]
        account = Account()
        account.set_account_number(account_number)
        account.set_currency(currency)
        account.set_balance(float(balance))
        return account
        
