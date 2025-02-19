from .repository import Repository
from mappers import TransactionMapper
from exceptions import NotEnoughMoneyException


class TransactionRepo(Repository):
    def __init__(self):
        super().__init__(TransactionMapper())

    def get_by_account(self, account_id):
        cursor = self.connection.cursor()

        self.begin(cursor)
        cursor.execute(
        """
        SELECT * FROM transaction 
        WHERE source_acc = %s OR destination_acc = %s 
        ORDER BY transaction_date DESC 
        LIMIT 50
        """,
            (account_id, account_id),
        )
        self.commit(cursor)
        return [self.map_to_dto(fetched) for fetched in self.connection.fetchall()]

    def get_by_id(self, id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT * FROM transaction 
            WHERE id = %s
        """,
            (id),
        )
        return self.connection.fetchone()

    def create_transaction(self, transaction):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO transaction (source_acc, destination_acc, currency, amount, label, transaction_date, type)
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
            cursor = self.connection.cursor()

            self.begin(cursor)
            cursor.execute(
                """
            UPDATE account 
            SET balance = balance - %s 
            WHERE id = %s
            """,
                (amount, source_acc),
            )

            cursor = self.connection.cursor()

            cursor.execute(
                """
            SELECT balance FROM account 
            WHERE id = %s
            """,
                (source_acc),
            )
            balance = self.connection.fetchone()[0]
            if balance < 0:
                raise NotEnoughMoneyException()

            cursor = self.connection.cursor()

            cursor.execute(
                """
            UPDATE account 
            SET balance = balance + %s 
            WHERE id = %s
            """,
                (amount, destination_acc),
            )

            cursor = self.connection.cursor()

            cursor.execute(
                """
            INSERT INTO transaction (source_acc, destination_acc, currency, amount, label, transaction_date, type)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id, source_acc, destination_acc, currency, amount, label, transaction_date, type
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
            transaction = self.map_to_dto( self.connection.fetchone() )
            self.commit(cursor)
            return transaction
        except Exception as e:
            self.rollback(cursor)
            raise e
