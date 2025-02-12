import connect_db as db

class CurrencyRepo:
    

    def get_currency(label):
        cursor = db.connect()
        cursor.execute("SELECT * FROM currency WHERE label = %s", (label,))
        return cursor.fetchone()

