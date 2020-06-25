import time
from database.stocks_database import StocksDatabase
from ..api_to_database_table.helpers.status import Status
from .alpha_vantage_to_daily_history import AlphaVantageToDailyHistory


class DailyHistoryUpdater:
    def __init__(self, database: StocksDatabase):
        self.db = database
        self.alpha_vantage_to_daily_history = AlphaVantageToDailyHistory(self.db)

    def update_stock(self):
        pass

    def update_all_stocks(self, days_old=7):
        tickers = self.db.api_progress_table.get_daily_history_progress(days_old)
        for ticker in tickers:
            status = self.alpha_vantage_to_daily_history.update_stock(ticker)
            print(status)
            if status == Status.Success or status == Status.Invalid:
                self.db.api_progress_table.update_daily_history_progress(ticker)
                time.sleep(15)  # API limits 5 calls per minute
                continue
            if status == Status.Failed:
                continue
            if status == Status.API_Limit:
                print('Stopping due to reaching APi limit')
                break
