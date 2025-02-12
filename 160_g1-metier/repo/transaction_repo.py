import connect_db as db


class TransactionRepo:
    def get_by_account(account_id):
        cursor = db.connect()
        cursor.execute("""
            SELECT * FROM transaction 
            WHERE source_acc = %s OR destination_acc = %s 
            ORDER BY transaction_date DESC 
            LIMIT 50
        """, (account_id, account_id))
        return cursor.fetchall()
    
    def get_by_id(id):
        curseur = db.connect()
        curseur.execute("""
            SELECT * FROM transaction 
            WHERE id = %s
        """, (id))
        return curseur.fetchone()

    def create_transaction(transaction):
        cursor = db.connect()
        cursor.execute("""
            INSERT INTO transaction (source_acc, destination_acc, currency, amount, label, transaction_date, type)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (transaction.source_acc, transaction.destination_acc, transaction.currency, transaction.amount, transaction.label, transaction.datetime, transaction.type))
        return cursor.lastrowid