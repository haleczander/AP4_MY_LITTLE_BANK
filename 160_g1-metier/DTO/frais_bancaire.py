class FraisBancaire:
    def __init__(self, id, montant, currency):
        self.id = id
        self.montant = montant
        self.currency = currency
    def get_id(self):
        return self.id
    def get_montant(self):
        return self.montant
    def get_currency(self):
        return self.currency