from .repository import Repository
from mappers import CurrencyRateMapper

class CurrencyRateRepo(Repository):
    def __init__(self):
        super().__init__(CurrencyRateMapper())

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