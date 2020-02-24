from database import postgres
from database import stocks_database

table_name = 'current_data'

def update_dividend_ttm(ticker, dividend_ttm):
    _update_row(ticker, 'dividend_ttm', dividend_ttm)

def update_dividend_yield(ticker, dividend_yield):
    _update_row(ticker, 'dividend_yield', dividend_yield)

def update_dividend_years(ticker, dividend_years):
    _update_row(ticker, 'dividend_years', dividend_years)

def update_dividend_years_increasing(ticker, dividend_years_increasing):
    _update_row(ticker, 'dividend_years_increasing', dividend_years_increasing)

def update_payout_ratio_ttm(ticker, payout_ratio_ttm):
    _update_row(ticker, 'payout_ratio_ttm', payout_ratio_ttm)

def update_price(ticker, price):
    _update_row(ticker, 'price', price)

def update_eps_ttm(ticker, eps):
    _update_row(ticker, 'eps_ttm', eps)

def _update_row(ticker, column, value):
    if value == None:
        return False
    return postgres.update_row(
        stocks_database.cursor, table_name, 'ticker', f"'{ticker}'", column, value)

def get_exchange(ticker):
    query = f"SELECT exchange FROM {table_name} WHERE ticker = '{ticker}'"
    postgres.run_query(stocks_database.cursor, query)
    exchange = postgres.get_list_results(stocks_database.cursor)[0]
    return exchange

def get_dividend_ttm(ticker):
    query = f"SELECT dividend_ttm FROM {table_name} WHERE ticker = '{ticker}'"
    postgres.run_query(stocks_database.cursor, query)
    dividend = postgres.get_list_results(stocks_database.cursor)[0]
    return dividend

def get_eps_ttm(ticker):
    query = f"SELECT eps_ttm FROM {table_name} WHERE ticker = '{ticker}'"
    postgres.run_query(stocks_database.cursor, query)
    eps_ttm = postgres.get_list_results(stocks_database.cursor)[0]
    return eps_ttm

def get_price(ticker):
    query = f"SELECT price FROM {table_name} WHERE ticker = '{ticker}'"
    postgres.run_query(stocks_database.cursor, query)
    price = postgres.get_list_results(stocks_database.cursor)[0]
    return price
