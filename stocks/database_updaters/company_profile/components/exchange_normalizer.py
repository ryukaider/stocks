from database.stocks_database import StocksDatabase

class ExchangeNormalizer:
    def __init__(self, database: StocksDatabase):
        self.db = database

    def normalize_all_exchanges(self):
        query = f'SELECT ticker FROM {self.db.company_profile_table.name}'
