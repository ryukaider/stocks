from database.stocks_database import StocksDatabase


class ApiProgressUpdater:
    def __init__(self, database: StocksDatabase):
        self.db = database

    def update_all_tickers(self, remove_delisted_rows=True):
        """
        Updates the api_progress table with the latest tickers from the tickers table,
        as well as removing any delisted tickers.
        """

        fresh_tickers = self._get_fresh_tickers()
        if remove_delisted_rows:
            self._remove_delisted_tickers(fresh_tickers)
        return self.db.api_progress_table.add_tickers(fresh_tickers)

    def _get_fresh_tickers(self):
        fresh_tickers = self.db.tickers_table.get_tickers()
        if fresh_tickers is None or len(fresh_tickers) == 0:
            raise Exception('Failed to get tickers from tickers table')
        return fresh_tickers

    def _remove_delisted_tickers(self, fresh_tickers):
        stale_tickers = self._get_stale_tickers()
        for ticker in stale_tickers:
            if ticker not in fresh_tickers:
                self.db.api_progress_table.delete_row('ticker', ticker)

    def _get_stale_tickers(self):
        api_progress_rows = self.db.api_progress_table.get_all_rows()
        stale_tickers = []
        for row in api_progress_rows:
            stale_tickers.append(row['ticker'])
        return stale_tickers
