from database_updaters.calculations import yearly_history_calculations
from database.stocks_database import StocksDatabase

db = StocksDatabase()


def update_all_stocks():
    update_end_prices()
    update_average_prices()
    update_dividends()
    update_average_dividend_yields()


def update_end_prices():
    tickers = db.tickers_table.get_tickers()
    for ticker in tickers:
        end_of_year_prices = yearly_history_calculations.calculate_end_of_year_prices(ticker)
        for year, price in end_of_year_prices.items():
            db.yearly_history_table.update_end_price(ticker, year, price)


def update_average_prices():
    tickers = db.tickers_table.get_tickers()
    for ticker in tickers:
        average_prices = yearly_history_calculations.calculate_average_prices(ticker)
        for year, price in average_prices.items():
            db.yearly_history_table.update_average_price(ticker, year, price)


def update_dividends():
    tickers = db.tickers_table.get_tickers()
    for ticker in tickers:
        dividends_by_year = yearly_history_calculations.calculate_dividends(ticker)
        for year, dividend in dividends_by_year.items():
            db.yearly_history_table.update_dividend(ticker, year, dividend)


def update_average_dividend_yields():
    tickers = db.tickers_table.get_tickers()
    for ticker in tickers:
        dividend_yields = yearly_history_calculations.calculate_average_dividend_yields(ticker)
        for year, dividend in dividend_yields.items():
            db.yearly_history_table.update_dividend_yield(ticker, year, dividend)


if __name__ == "__main__":
    update_all_stocks()
