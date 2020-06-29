import datetime
from database.stocks_database import StocksDatabase


class YearlyHistoryCalculator:

    default_start_year = 2000

    def __init__(self, database: StocksDatabase):
        self.db = database

    def calculate_end_of_year_prices(self, ticker, start_year=default_start_year):
        yearly_prices = {}
        current_year = datetime.datetime.now().year
        for year in range(start_year, current_year):
            price = self.calculate_end_of_year_price(ticker, year)
            yearly_prices[year] = price
        return yearly_prices

    def calculate_end_of_year_price(self, ticker, year):
        query = f"SELECT adjusted_close " \
                f"FROM {self.db.daily_history_table.name} " \
                f"WHERE ticker = '{ticker}' " \
                f"AND date >= '{year}-01-01' " \
                f"AND date <= '{year}-12-31' " \
                f"ORDER BY date desc " \
                f"LIMIT 1"
        result = self.db.daily_history_table.run_query(query)
        if len(result) == 0:
            return None
        return result[0]['adjusted_close']

    def calculate_average_prices(self, ticker, start_year=default_start_year):
        average_prices = {}
        current_year = datetime.datetime.now().year
        for year in range(start_year, current_year):
            price = self.calculate_average_price(ticker, year)
            average_prices[year] = price
        return average_prices

    def calculate_average_price(self, ticker, year):
        query = f"SELECT adjusted_close " \
                f"FROM {self.db.daily_history_table.name} " \
                f"WHERE ticker = '{ticker}' " \
                f"AND date >= '{year}-01-01' " \
                f"AND date <= '{year}-12-31' " \
                f"ORDER BY date desc"
        rows = self.db.daily_history_table.run_query(query)
        row_count = len(rows)
        sum_price = 0
        if row_count == 0:
            return None
        for row in rows:
            sum_price += row['adjusted_close']
        average = sum_price / row_count
        return float(average)

    def calculate_dividends(self, ticker, start_year=default_start_year):
        dividends = {}
        current_year = datetime.datetime.now().year
        for year in range(start_year, current_year):
            dividend = self.calculate_dividend(ticker, year)
            dividends[year] = float(dividend)
        return dividends

    def calculate_dividend(self, ticker, year):
        query = f"SELECT dividend " \
                f"FROM {self.db.daily_history_table.name} " \
                f"WHERE ticker = '{ticker}' " \
                f"AND date >= '{year}-01-01' " \
                f"AND date <= '{year}-12-31' " \
                f"AND dividend > 0 " \
                f"ORDER BY date desc"
        rows = self.db.daily_history_table.run_query(query)
        dividend = 0
        for row in rows:
            dividend += row['dividend']
        return float(dividend)

    def calculate_average_dividend_yields(self, ticker, start_year=default_start_year):
        dividend_yields = {}
        current_year = datetime.datetime.now().year
        for year in range(start_year, current_year):
            dividend = self.db.yearly_history_table.get_dividend(ticker, year)
            average_price = self.db.yearly_history_table.get_average_price(ticker, year)
            try:
                average_dividend_yield = (dividend / average_price) * 100
            except Exception:
                average_dividend_yield = 0
            dividend_yields[year] = float(average_dividend_yield)
        return dividend_yields
