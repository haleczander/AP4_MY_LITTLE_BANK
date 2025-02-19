class Transaction:
    def __init__(self):
        pass

    def set_id_transaction(self, id):
        self.id = id
        
    def set_source(self, source):
        self.source = source
        
    def set_destination(self, destination):
        self.destination = destination
        
    def set_amount(self, amount):
        self.amount = amount
        
    def set_currency(self, currency):
        self.currency = currency
        
    def set_label(self, label):
        self.label = label
        
    def set_type(self, type):
        self.type = type
        
    def set_datetime(self, datetime):
        self.datetime = datetime
        

    def get_id_transaction(self):
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
