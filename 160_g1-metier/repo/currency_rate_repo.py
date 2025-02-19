from .repository import Repository
from mappers import CurrencyRateMapper

class CurrencyRateRepo(Repository):
    ALL_FIELDS = ["from_currency", "to_currency", "rate"]

    def __init__(self):
        super().__init__(CurrencyRateMapper())

    def _all_fields(self):
        return ", ".join(self.ALL_FIELDS)

    def set_currency_rate(self, currency, target_currency, rate):
        cursor = self.connection.cursor()
        self.begin(cursor)
        cursor.execute(
            f"""
            INSERT INTO exchange_rate (from_currency, to_currency, rate) 
            VALUES ( %s, %s, %s )
            RETURNING exchange_rate_id, {self._all_fields()}
            """,
            (currency, target_currency, rate),
        )
        self.commit(cursor)
        result = cursor.fetchone() if cursor.description else None
        return self.map_to_dto(result)
