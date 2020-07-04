from database.stocks_database import StocksDatabase
from .yearly_history_calculator import YearlyHistoryCalculator


class YearlyHistoryUpdater:
    def __init__(self, database: StocksDatabase):
        self.db = database
        self.yearly_history_calculator = YearlyHistoryCalculator(self.db)

    def update_all(self):
        """
        Updates all yearly history data for all stocks, using calculations.
        """

        tickers = self.db.tickers_table.get_tickers()
        for ticker in tickers:
            self.update(ticker)

    def update(self, ticker):
        self.update_end_prices(ticker)
        self.update_average_prices(ticker)
        self.update_dividends(ticker)
        self.update_average_dividend_yields(ticker)

    def update_end_prices(self, ticker):
        end_of_year_prices = self.yearly_history_calculator.calculate_end_of_year_prices(ticker)
        for year, price in end_of_year_prices.items():
            self.db.yearly_history_table.update_end_price(ticker, year, price)

    def update_average_prices(self, ticker):
        average_prices = self.yearly_history_calculator.calculate_average_prices(ticker)
        for year, price in average_prices.items():
            self.db.yearly_history_table.update_average_price(ticker, year, price)

    def update_dividends(self, ticker):
        dividends_by_year = self.yearly_history_calculator.calculate_dividends(ticker)
        for year, dividend in dividends_by_year.items():
            self.db.yearly_history_table.update_dividend(ticker, year, dividend)

    def update_average_dividend_yields(self, ticker):
        dividend_yields = self.yearly_history_calculator.calculate_average_dividend_yields(ticker)
        for year, dividend in dividend_yields.items():
            self.db.yearly_history_table.update_dividend_yield(ticker, year, dividend)
