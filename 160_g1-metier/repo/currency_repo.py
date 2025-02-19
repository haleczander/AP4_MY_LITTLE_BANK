from .repository import Repository
from mappers import CurrencyMapper


class CurrencyRepo(Repository):
    def __init__(self):
        super().__init__(CurrencyMapper())

    def get_currencies(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM currency")
            results = cursor.fetchall() if cursor.description else []
            return [self.mapper.map_to_dto(row) for row in results]
        except Exception as e:
            self.rollback(cursor)
            raise e

    def get_currency(self, label):
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM currency WHERE code = %s", (label,))
        result = cursor.fetchone() if cursor.description else None

        return self.mapper.map_to_dto(result)
