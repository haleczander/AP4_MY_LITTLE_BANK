from .repository import Repository
from mappers import AccountMapper



class AccountRepo(Repository):
    ALL_FIELDS = ["account_number", "balance", "currency"]

    def __init__(self):
        super().__init__(AccountMapper())
        
    def _all_fields(self):
        return ", ".join(self.ALL_FIELDS)

    # create
    def create_account(self, balance, currency):
        self.begin()
        self.connection.execute(
            """
            INSERT INTO account (balance, currency) 
            VALUES (%s, %s) 
            RETURNING account_number, balance, currency
            """,
            (balance, currency),
        )
        self.commit()
    
        return self.map_to_dto(self.connection.fetchone())

    # read
    def find_by_id(self, id):
        
        self.connection.execute(
            f"""
            SELECT {self._all_fields()} 
            FROM account 
            WHERE account_number = %s
            """
            , (id,))
        return self.map_to_dto( self.connection.fetchone() )

    def get_balance(self, id):

        self.connection.execute(
            f"""
            SELECT balance 
            FROM account 
            WHERE account_number = %s
            """, (id,))
        
        res = self.connection.fetchall()
        return None if not res else res[0][0]

    # update
    def update_account(self, id, balance, currency):
        self.begin()
        self.connection.execute(
            f"""
            UPDATE account 
            SET balance = %s, currency = %s 
            WHERE account_number = %s
            RETURNING {self._all_fields()}
            """,
            (balance, currency, id),
        )
        self.commit()
        return self.map_to_dto( self.connection.fetchone() )


    # delete
    def delete_account(self, id):

        self.connection.execute(
            f"""
            DELETE 
            FROM account 
            WHERE account_number = %s
            """, (id,))
        return 
