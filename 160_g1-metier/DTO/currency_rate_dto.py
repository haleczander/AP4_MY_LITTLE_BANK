class CurrencyRate:
    def __init__(self):
        pass
    
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id

    def get_ref_currency(self):
        return self.ref_currency

    def get_other_currency(self):
        return self.other_currency

    def get_rate(self):
        return self.rate

    def set_ref_currency(self, ref_currency):
        self.ref_currency = ref_currency

    def set_other_currency(self, other_currency):
        self.other_currency = other_currency

    def set_rate(self, rate):
        self.rate = rate
