import time
from database_updaters.daily_history.helpers.status import Status
from .alpha_vantage_to_daily_history import AlphaVantageToDailyHistory
from .adjusted_dividends_calculator import AdjustedDividendsCalculator
from database.stocks_database import StocksDatabase


class DailyHistoryUpdater:
    def __init__(self, database: StocksDatabase):
        self.db = database
        self.alpha_vantage_to_daily_history = AlphaVantageToDailyHistory(self.db)
        self.adjusted_dividends_calculator = AdjustedDividendsCalculator()

    def update_all(self, days_old=7):
        """
        Updates daily history data for all stocks, using Alpha Vantage APIs + calculations.
        """

        tickers = self.db.api_progress_table.get_daily_history_progress(days_old)
        for ticker in tickers:
            status = self.alpha_vantage_to_daily_history.update_stock(ticker)
            print(status)
            if status == Status.Success or status == Status.Invalid:
                self.db.api_progress_table.update_daily_history_progress(ticker)
                self._update_adjusted_dividends(ticker)
                time.sleep(12)  # API limits 5 calls per minute
                continue
            if status == Status.Failed:
                continue
            if status == Status.API_Limit:
                print('Stopping due to reaching APi limit')
                break

    def update(self, ticker):
        status = self.alpha_vantage_to_daily_history.update_stock(ticker)
        print(status)
        if status == Status.Success or status == Status.Invalid:
            self.db.api_progress_table.update_daily_history_progress(ticker)
            self._update_adjusted_dividends(ticker)

    def _update_adjusted_dividends(self, ticker):
        daily_history_rows = self.db.daily_history_table.get_history(ticker)
        adjusted_dividend_rows = self.adjusted_dividends_calculator.calculate(daily_history_rows)
        return self.db.daily_history_table._upsert_rows(adjusted_dividend_rows)
