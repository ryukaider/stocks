import sys
sys.path.append('E:/Google Drive/Computers/Dev/Stocks/scott_stocks')

from database import postgres
from database import stocks_database
from database.tables import tickers_table

table_name = 'api_progress'

def reset_all():
    ticker_list = tickers_table.get_tickers()
    for ticker in ticker_list:
        if not add_stock(ticker):
            reset_monthly_progress(ticker)
            reset_eps_progress(ticker)

def add_stock(ticker):
    return postgres.insert_row(
        stocks_database.cursor,
        table_name,
        '(ticker, monthly, eps)',
        f"('{ticker}',false,false)")

def reset_monthly_progress(ticker):
    _update_progress(ticker, 'monthly', False)

def set_monthly_done(ticker):
    _update_progress(ticker, 'monthly', True)

def reset_eps_progress(ticker):
    _update_progress(ticker, 'eps', False)

def set_eps_done(ticker):
    _update_progress(ticker, 'eps', True)

def _update_progress(ticker, column, value):
    postgres.update_row(
        stocks_database.cursor, table_name, 'ticker', f"'{ticker}'", column, value)

def get_incomplete_stocks(column):
    query = f"SELECT ticker FROM {table_name} WHERE {column} is not true ORDER BY ticker ASC"
    postgres.run_query(stocks_database.cursor, query)
    tickers = postgres.get_list_results(stocks_database.cursor)
    return tickers

if __name__ == "__main__":
    reset_all()
