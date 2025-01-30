class Account:
    def __init__(self, id, sold, currency):
        self.id = id
        self.sold = sold
        self.currency = currency
    def get_id(self):
        return self.id
    def get_sold(self):
        return self.sold
    def get_currency(self):
        return self.currency