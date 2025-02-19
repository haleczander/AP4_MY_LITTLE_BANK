from .repository import Repository
from mappers import TransactionMapper
from exceptions import NotEnoughMoneyException
from psycopg2.extras import RealDictCursor



class TransactionRepo(Repository):
    def __init__(self):
        super().__init__(TransactionMapper())

    def get_by_account(self, account_id):
        cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        self.begin(cursor)
        cursor.execute(
        """
        SELECT transaction_id, type, dest_account, amount, currency, label, source_account, timestamp
        FROM transaction
        WHERE source_account = %s 
        ORDER BY timestamp DESC 
        LIMIT 50
        """,
            (account_id,),
        )
        results = cursor.fetchall() if cursor.description else []
        self.commit(cursor)
        return [self.map_to_dto(fetched) for fetched in results]

    def get_by_id(self, id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT * FROM transaction 
            WHERE transaction_id = %s
        """,
            (id),
        )
        result = cursor.fetchone() if cursor.description else None
        return self.map_to_dto(result)

    def create_transaction(self, transaction):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO transaction (source_account, destination_account, currency, amount, label, timestamp, type)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
            (
                transaction.source_acc,
                transaction.destination_acc,
                transaction.currency,
                transaction.amount,
                transaction.label,
                transaction.datetime,
                transaction.type,
            ),
        )
        return self.connection.lastrowid

    def execute_transaction(
        self,
        source_acc,
        destination_acc,
        currency,
        amount,
        label,
        transaction_date,
        type,
    ):
        try:
            cursor = self.connection.cursor(cursor_factory=RealDictCursor)

            self.begin(cursor)
            cursor.execute(
                """
            UPDATE account 
            SET balance = balance - %s 
            WHERE account_number = %s
            """,
                (amount, source_acc),
            )

            cursor.execute(
                """
            UPDATE account 
            SET balance = balance + %s 
            WHERE account_number = %s
            """,
                (amount, destination_acc),
            )
            
            cursor.execute(
            """
                SELECT balance 
                FROM account 
                WHERE account_number = %s
            """,
                (source_acc,),
            )
            balance = cursor.fetchone()["balance"] if cursor.description else None
            if not balance:
                raise Exception("Account not found")
            elif balance < 0:
                self.rollback(cursor)
                return 
                # raise NotEnoughMoneyException()

            cursor.execute(
                """
            INSERT INTO transaction (source_account, dest_account, currency, amount, label, timestamp, type)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING transaction_id, source_account, dest_account, currency, amount, label, timestamp, type
            """,
                (
                    source_acc,
                    destination_acc,
                    currency,
                    amount,
                    label,
                    transaction_date,
                    type,
                ),
            )


            cursor.execute(
                """
            INSERT INTO transaction (dest_account, source_account, currency, amount, label, timestamp, type)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING transaction_id, source_account, dest_account, currency, amount, label, timestamp, type
            """,
                (
                    source_acc,
                    destination_acc,
                    currency,
                    -amount,
                    label,
                    transaction_date,
                    type,
                ),
            )
            result = cursor.fetchone() if cursor.description else None
            transaction = self.map_to_dto( result )
            self.commit(cursor)
            return transaction
        except Exception as e:
            self.rollback(cursor)
            raise e
