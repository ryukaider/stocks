from database_updaters.calculations import daily_history_calculations
from databases.stocks_database import StocksDatabase


class CalculationsToDailyHistory:
    def __init__(self, database: StocksDatabase):
        self.db = database

    def update_all_adjusted_dividends(self):
        tickers = self.db.tickers_table.get_tickers()
        for ticker in tickers:
            self.update_adjusted_dividend(ticker)

    def update_adjusted_dividend(self, ticker):
        daily_history_rows = self.db.daily_history_table.get_history(ticker)
        adjusted_dividend_rows = daily_history_calculations.calculate_adjusted_dividends(daily_history_rows)
        return self.db.daily_history_table.upsert_rows(adjusted_dividend_rows)


if __name__ == '__main__':
    CalculationsToDailyHistory(StocksDatabase()).update_adjusted_dividend('A')
