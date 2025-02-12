from repository import Repository

class CurrencyRepo(Repository):
    def __init__(self):
        super().__init__()
    

    def get_currency(self, label):
        
        self.connection.execute("SELECT * FROM currency WHERE label = %s", (label,))
        return self.connection.fetchone()

