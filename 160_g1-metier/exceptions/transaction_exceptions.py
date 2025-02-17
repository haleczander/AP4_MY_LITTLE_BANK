class NotEnoughMoneyException(Exception):
    def __init__(self, *args):
        super().__init__("Not enough money on the account")
