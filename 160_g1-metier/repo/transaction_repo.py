from .repository import Repository
from mappers import TransactionMapper
from exceptions import NotEnoughMoneyException


class TransactionRepo(Repository):
    def __init__(self):
        super().__init__(TransactionMapper())

    def get_by_account(self, account_id):

        self.connection.execute(
            """
            SELECT * FROM transaction 
            WHERE source_acc = %s OR destination_acc = %s 
            ORDER BY transaction_date DESC 
            LIMIT 50
        """,
            (account_id, account_id),
        )
        return self.connection.fetchall()

    def get_by_id(self, id):
        self.connection.execute(
            """
            SELECT * FROM transaction 
            WHERE id = %s
        """,
            (id),
        )
        return self.connection.fetchone()

    def create_transaction(self, transaction):
        self.connection.execute(
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
            self.connection.begin()
            self.connection.execute(
                """
            UPDATE account 
            SET balance = balance - %s 
            WHERE id = %s
            """,
                (amount, source_acc),
            )

            self.connection.execute(
                """
            SELECT balance FROM account 
            WHERE id = %s
            """,
                (source_acc),
            )
            balance = self.connection.fetchone()[0]
            if balance < 0:
                raise NotEnoughMoneyException()

            self.connection.execute(
                """
            UPDATE account 
            SET balance = balance + %s 
            WHERE id = %s
            """,
                (amount, destination_acc),
            )

            self.connection.execute(
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
            self.connection.commit()
            return transaction
        except Exception as e:
            self.connection.rollback()
            raise e
