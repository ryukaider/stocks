from databases.stocks_database import StocksDatabase
from web_apis import nasdaq


class NasdaqToTickers:
    def __init__(self, database: StocksDatabase):
        self.db = database

    def update_all_tickers(self, remove_existing_rows=True):
        tickers = nasdaq.get_all_tickers()
        if remove_existing_rows:
            self.db.tickers_table.delete_all_rows()
        return self.db.tickers_table.add_tickers(tickers)
