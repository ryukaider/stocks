from databases.stocks_database import StocksDatabase
from database_updaters.api_to_database_table.nasdaq_to_tickers import NasdaqToTickers


class DatabaseUpdater:
    def __init__(self, database: StocksDatabase):
        self.db = database

        self.nasdaq_to_tickers = NasdaqToTickers(self.db)
