class Transaction:
    def __init__(self, id, source_acc, destination_acc, currency, amount, label, type):
        self.id = id
        self.source = source_acc
        self.destination = destination_acc
        self.currency = currency
        self.amount = amount
        self.label = label
        self.type = type
    def get_id(self):
        return self.id
    def get_source(self):
        return self.source
    def get_destination(self):
        return self.destination
    def get_amount(self):
        return self.amount
    def get_currency(self):
        return self.currency
    def get_label(self):
        return self.label
    def get_type(self):
        return self.type