import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(_root_path)

from database import postgres
from database import stocks_database
from database.tables import tickers_table


table_name = 'api_progress'

columns = {
    'ticker': 'text PRIMARY KEY',
    'monthly': 'boolean',
    'eps': 'boolean'
}

cursor = stocks_database.get_cursor()


def exists():
    return postgres.table_exists(cursor, table_name)


def create():
    if not exists():
        return postgres.create_table(cursor, table_name, columns)
    return exists()


def reset_all():
    ticker_list = tickers_table.get_tickers()
    for ticker in ticker_list:
        if not add_stock(ticker):
            reset_monthly_progress(ticker)
            reset_eps_progress(ticker)


def add_stock(ticker):
    return postgres.insert_row(
        cursor,
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
        cursor, table_name, 'ticker', f"'{ticker}'", column, value)


def get_incomplete_stocks(column):
    query = f"SELECT ticker FROM {table_name} WHERE {column} is not true ORDER BY ticker ASC"
    postgres.run_query(cursor, query)
    tickers = postgres.get_list_results(cursor)
    return tickers


create()
