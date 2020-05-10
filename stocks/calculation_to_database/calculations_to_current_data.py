from databases.tables.tickers_table import TickersTable
from databases.tables.current_data_table import CurrentDataTable
from databases.tables.monthly_history_table import MonthlyHistoryTable
from calculations import current_data_calculations

tickers_table = TickersTable()
current_data_table = CurrentDataTable()
monthly_history_table = MonthlyHistoryTable()


def update_all():
    update_all_latest_price()
    update_all_dividend_ttm()
    update_all_dividend_yield()
    update_all_dividend_years()
    update_all_dividend_years_increasing()
    update_all_payout_ratio_ttm()


def update_all_latest_price():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        update_latest_price(ticker)


def update_latest_price(ticker):
    price = monthly_history_table.get_latest_price(ticker)
    current_data_table.update_price(ticker, price)


def update_all_dividend_ttm():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        update_dividend_ttm(ticker)


def update_dividend_ttm(ticker):
    dividend = current_data_calculations.calculate_dividend_ttm(ticker)
    dividend = round(dividend, 2)
    current_data_table.update_dividend_ttm(ticker, dividend)


def update_all_dividend_yield():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        update_dividend_yield(ticker)
    

def update_dividend_yield(ticker):
    dividend_yield = current_data_calculations.calculate_dividend_yield(ticker)
    current_data_table.update_dividend_yield(ticker, dividend_yield)


def update_all_dividend_years():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        update_dividend_years(ticker)
    

def update_dividend_years(ticker):
    dividend_years = current_data_calculations.calculate_years_of_dividends(ticker)
    current_data_table.update_dividend_years(ticker, dividend_years)


def update_all_dividend_years_increasing():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        update_dividend_years_increasing(ticker)
    

def update_dividend_years_increasing(ticker):
    dividend_increasing_years = current_data_calculations.calculate_years_of_dividends_increasing(ticker)
    current_data_table.update_dividend_years_increasing(ticker, dividend_increasing_years)


def update_all_payout_ratio_ttm():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        update_payout_ratio_ttm(ticker)


def update_payout_ratio_ttm(ticker):
    payout_ratio_ttm = current_data_calculations.calculate_payout_ratio_ttm(ticker)
    current_data_table.update_payout_ratio_ttm(ticker, payout_ratio_ttm)


if __name__ == "__main__":
    update_all()
