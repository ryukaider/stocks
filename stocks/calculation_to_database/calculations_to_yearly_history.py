from databases.tables.tickers_table import TickersTable
from databases.tables.yearly_history_table import YearlyHistoryTable
from calculations import yearly_history_calculations

tickers_table = TickersTable()
yearly_history_table = YearlyHistoryTable()


def update_all_stocks():
    update_end_price()
    update_average_price()
    update_annual_dividends()
    update_dividend_yields()


def update_end_price():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        end_of_year_prices = yearly_history_calculations.calculate_end_of_year_prices(ticker)
        for year, price in end_of_year_prices.items():
            yearly_history_table.update_end_price(ticker, year, price)


def update_average_price():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        average_prices = yearly_history_calculations.calculate_average_prices(ticker)
        for year, price in average_prices.items():
            yearly_history_table.update_average_price(ticker, year, price)


def update_annual_dividends():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        dividends_by_year = yearly_history_calculations.calculate_dividend(ticker)
        for year, dividend in dividends_by_year.items():
            yearly_history_table.update_dividend(ticker, year, dividend)


def update_dividend_yields():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        dividend_yields = yearly_history_calculations.calculate_dividend_yield(ticker)
        for year, dividend in dividend_yields.items():
            yearly_history_table.update_dividend_yield(ticker, year, dividend)


if __name__ == "__main__":
    update_all_stocks()
