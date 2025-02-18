from .repository import Repository
from mappers import CurrencyMapper


class CurrencyRepo(Repository):
    def __init__(self):
        super().__init__(CurrencyMapper())

    def get_currencies(self):
        try:
            self.connection.execute("SELECT * FROM currency")
            return [self.mapper.map_to_dto(row) for row in self.connection.fetchall()]
        except Exception as e:
            self.connection.execute("ROLLBACK")
            raise e

    def get_currency(self, label):
        self.connection.execute("SELECT * FROM currency WHERE code = %s", (label,))
        return self.mapper.map_to_dto(self.connection.fetchone())
