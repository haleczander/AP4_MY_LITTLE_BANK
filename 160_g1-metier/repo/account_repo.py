from .repository import Repository


class AccountRepo(Repository):
    def __init__(self):
        super().__init__()

    # create
    def create_account(self, id, sold, currency):

        self.connection.execute(
            "INSERT INTO account (id, sold, currency) VALUES (%s, %s, %s)",
            (id, sold, currency),
        )
        self.connection.commit()
        return 0

    # read
    def find_by_id(self, id):

        self.connection.execute("SELECT * FROM account WHERE id = %s", (id,))
        return self.connection.fetchone()

    def get_balance(self, id):

        self.connection.execute("SELECT sold FROM account WHERE id = %s", (id,))
        return self.connection.fetchone()

    # update
    def update_account(self, id, sold, currency):

        self.connection.execute(
            "UPDATE account SET sold = %s, currency = %s WHERE id = %s",
            (sold, currency, id),
        )
        self.connection.commit()
        return 0

    # delete
    def delete_account(self, id):

        self.connection.execute("DELETE FROM account WHERE id = %s", (id,))
        self.connection.commit()
        return 0
