from .repository import Repository
from mappers import CurrencyRateMapper

class CurrencyRateRepo(Repository):
    ALL_FIELDS = ["currency", "target_currency", "rate"]

    def __init__(self):
        super().__init__(CurrencyRateMapper())

    def _all_fields(self):
        return ", ".join(self.ALL_FIELDS)

    def set_currency_rate(self, currency, target_currency, rate):
        self.begin()
        self.connection.execute(
            f"""
            INSERT INTO currency_rate (currency, target_currency, rate) 
            VALUES ( %s, %s, %s )
            RETURNING {self._all_fields()}
            """,
            (currency, target_currency, rate),
        )
        self.commit()
        return self.map_to_dto( self.connection.fetchone() )