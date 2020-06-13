from databases.stocks_database import StocksDatabase
from web_apis import nasdaq


class NasdaqToTickers:
    def __init__(self, database: StocksDatabase):
        self.db = database

    def update_all_tickers(self, delete_existing_rows=True):
        tickers = nasdaq.get_all_tickers()
        if tickers is None or len(tickers) == 0:
            raise Exception('Failed to retrieve tickers from Nasdaq FTP site')
        if delete_existing_rows:
            self.db.tickers_table.delete_all_rows()
        return self.db.tickers_table.add_tickers(tickers)
