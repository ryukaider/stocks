from databases.stocks_database import StocksDatabase
from web_apis import nasdaq


class NasdaqToTickers:
    def __init__(self, database: StocksDatabase):
        self.db = database

    def update_all_tickers(self):
        tickers = nasdaq.get_all_tickers()
        self.db.tickers_table.delete_all_rows()
        self.db.tickers_table.add_tickers(tickers)
