import connect_db as db


class AccountRepo:
    #create
    def create_account(id, sold, currency):
        cursor = db.connect()
        cursor.execute("INSERT INTO account (id, sold, currency) VALUES (%s, %s, %s)", (id, sold, currency))
        cursor.commit()
        return 0

    #read
    def find_by_id(id):
        cursor = db.connect()
        cursor.execute("SELECT * FROM account WHERE id = %s", (id,))
        return cursor.fetchone()


    def get_balance(id):
        cursor = db.connect()
        cursor.execute("SELECT sold FROM account WHERE id = %s", (id,))
        return cursor.fetchone()


    #update
    def update_account(id, sold, currency):
        cursor = db.connect()
        cursor.execute("UPDATE account SET sold = %s, currency = %s WHERE id = %s", (sold, currency, id))
        cursor.commit()
        return 0

    #delete
    def delete_account(id):
        cursor = db.connect()
        cursor.execute("DELETE FROM account WHERE id = %s", (id,))
        cursor.commit()
        return 0