import datetime
from database.stocks_database import StocksDatabase


class DividendsUpdater:
    def __init__(self, database: StocksDatabase):
        self.db = database

    def update_all(self):
        """
        Updates all dividend data for all stocks, using calculations
        """

        self.update_dividend_years()
        self.update_dividend_years_stable()
        self.update_dividend_years_increasing()
        self.update_dividend_ttm()
        self.update_dividend_yield_ttm()

    def update_dividend_years(self):
        tickers = self.db.tickers_table.get_tickers()
        for ticker in tickers:
            self.db.dividends_table.add_stock(ticker)
            dividend_years = self.calculate_dividend_years(ticker)
            self.db.dividends_table.update_dividend_years(ticker, dividend_years)

    def calculate_dividend_years(self, ticker):
        data = self.db.yearly_history_table.get_data(ticker)
        years = 0
        for row in data:
            if row['dividend'] is None and years == 0:
                continue
            if row['dividend'] is None:
                break
            if row['dividend'] > 0:
                years += 1
            else:
                break
        return years

    def update_dividend_years_stable(self):
        tickers = self.db.tickers_table.get_tickers()
        for ticker in tickers:
            self.db.dividends_table.add_stock(ticker)
            dividend_years_stable = self.calculate_dividend_years_stable(ticker)
            self.db.dividends_table.update_dividend_years_stable(ticker, dividend_years_stable)

    def calculate_dividend_years_stable(self, ticker):
        data = self.db.yearly_history_table.get_data(ticker)
        years = 0
        previous_year_dividend = None
        for row in data:
            if row['dividend'] is None and years == 0:
                continue
            if row['dividend'] is None:
                break
            if row['dividend'] > 0 and (previous_year_dividend is None or previous_year_dividend >= row['dividend']):
                years += 1
                previous_year_dividend = row['dividend']
            else:
                break
        return years

    def update_dividend_years_increasing(self):
        tickers = self.db.tickers_table.get_tickers()
        for ticker in tickers:
            self.db.dividends_table.add_stock(ticker)
            dividend_years_increasing = self.calculate_years_of_dividends_increasing(ticker)
            self.db.dividends_table.update_dividend_years_increasing(ticker, dividend_years_increasing)

    def calculate_years_of_dividends_increasing(self, ticker):
        data = self.db.yearly_history_table.get_data(ticker)
        years = 0
        previous_year_dividend = None
        for row in data:
            if row['dividend'] is None and years == 0:
                continue
            if row['dividend'] is None:
                break
            if row['dividend'] > 0 and (previous_year_dividend is None or previous_year_dividend > row['dividend']):
                years += 1
                previous_year_dividend = row['dividend']
            else:
                break
        return years

    def update_dividend_yield_ttm(self):
        tickers = self.db.tickers_table.get_tickers()
        for ticker in tickers:
            self.db.dividends_table.add_stock(ticker)
            dividend_yield_ttm = self.calculate_dividend_yield_ttm(ticker)
            self.db.dividends_table.update_dividend_yield_ttm(ticker, dividend_yield_ttm)

    def calculate_dividend_yield_ttm(self, ticker):
        history = self.db.daily_history_table.get_history(ticker)
        dividend_yield_ttm = 0
        try:
            latest_price = history[0]['adjusted_close']
            dividend_ttm = self.db.dividends_table.get_dividend_ttm(ticker)
            dividend_yield_ttm = (float(dividend_ttm) / float(latest_price)) * 100
        except Exception:
            pass
        return dividend_yield_ttm

    def update_dividend_ttm(self):
        tickers = self.db.tickers_table.get_tickers()
        for ticker in tickers:
            self.db.dividends_table.add_stock(ticker)
            dividend_ttm = self.calculate_dividend_ttm(ticker)
            self.db.dividends_table.update_dividend_ttm(ticker, dividend_ttm)

    def calculate_dividend_ttm(self, ticker):
        start_date = (datetime.datetime.now() - datetime.timedelta(days=365)).date()
        query = f"SELECT dividend FROM {self.db.daily_history_table.name} " \
                f"WHERE ticker = '{ticker}' " \
                f"AND date >= '{start_date}' " \
                f"AND dividend != 0"
        rows = self.db.daily_history_table.run_query(query)
        dividend_ttm = 0
        for row in rows:
            dividend_ttm += row['dividend']
        return dividend_ttm
