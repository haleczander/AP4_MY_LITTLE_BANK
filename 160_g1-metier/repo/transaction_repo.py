from repository import Repository


class TransactionRepo(Repository):
    def __init__(self):
        super().__init__()

    def get_by_account(self, account_id):
        
        self.connection.execute("""
            SELECT * FROM transaction 
            WHERE source_acc = %s OR destination_acc = %s 
            ORDER BY transaction_date DESC 
            LIMIT 50
        """, (account_id, account_id))
        return self.connection.fetchall()
    
    def get_by_id(self,  id):
        self.connection.execute("""
            SELECT * FROM transaction 
            WHERE id = %s
        """, (id))
        return self.connection.fetchone()

    def create_transaction(self, transaction):
        
        self.connection.execute("""
            INSERT INTO transaction (source_acc, destination_acc, currency, amount, label, transaction_date, type)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (transaction.source_acc, transaction.destination_acc, transaction.currency, transaction.amount, transaction.label, transaction.datetime, transaction.type))
        return self.connection.lastrowid