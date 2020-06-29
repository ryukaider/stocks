import datetime
from database.stocks_database import StocksDatabase
from web_apis import nasdaq


class TickersUpdater:
    def __init__(self, database: StocksDatabase):
        self.db = database

    def update_all_tickers(self, remove_existing_rows=True, days_old=1):
        """
        Updates tickers table with the latest tickers from the Nasdaq ftp site.
        """

        if not self._is_updatable(days_old):
            return False
        tickers = nasdaq.get_all_tickers()
        if remove_existing_rows:
            self.db.tickers_table.delete_all_rows()
        success = self.db.tickers_table.add_tickers(tickers)
        if success:
            self.db.table_progress_table.add_row(self.db.tickers_table.name)
            self.db.table_progress_table.update_progress(self.db.tickers_table.name)
        return success

    def _is_updatable(self, days_old):
        last_updated = self.db.table_progress_table.get_last_updated(self.db.tickers_table.name)
        if last_updated is None:
            return True
        last_updated_delta = (datetime.datetime.now().date() - last_updated)
        if last_updated_delta >= datetime.timedelta(days=days_old):
            return True
        return False
