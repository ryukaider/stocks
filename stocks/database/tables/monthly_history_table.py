import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(_root_path)

from database import postgres
from database import stocks_database


table_name = 'monthly_history'

columns = {
    'ticker': 'text NOT NULL',
    'date': 'date NOT NULL',
    'price': 'double precision',
    'dividend': 'double precision',
    'CONSTRAINT pk_ticker_date': 'PRIMARY KEY (ticker, date)'
}

cursor = stocks_database.get_cursor()


def exists():
    return postgres.table_exists(cursor, table_name)


def create():
    if not exists():
        return postgres.create_table(cursor, table_name, columns)
    return exists()


def add_monthly_data(monthly_data):
    for row in monthly_data:
        add_monthly_row(row)


def add_monthly_row(monthly_row):
    if not postgres.insert_row(stocks_database.cursor, table_name, '(ticker, date, price, dividend)',
        f"('{monthly_row['ticker']}','{monthly_row['date']}','{monthly_row['price']}','{monthly_row['dividend']}')"):
        update_query = f"UPDATE {table_name} SET price = '{monthly_row['price']}' WHERE ticker = '{monthly_row['ticker']}' AND date = '{monthly_row['date']}'"
        postgres.run_query(stocks_database.cursor, update_query)


def get_history(ticker):
    query = f"SELECT * FROM {table_name} WHERE ticker = '{ticker}' ORDER BY date DESC"
    postgres.run_query(stocks_database.cursor, query)
    data = stocks_database.cursor.fetchall()
    return data


def get_date_dividend(ticker):
    query = f"SELECT date,dividend FROM {table_name} WHERE ticker = '{ticker}' ORDER BY date DESC"
    postgres.run_query(stocks_database.cursor, query)
    data = stocks_database.cursor.fetchall()
    return data


def get_dividend_ttm(ticker):
    query = f"SELECT dividend FROM {table_name} WHERE ticker = '{ticker}' ORDER BY date DESC LIMIT 12"
    postgres.run_query(stocks_database.cursor, query)
    dividends = postgres.get_list_results(stocks_database.cursor)
    return dividends


def get_latest_price(ticker):
    query = f"SELECT price FROM {table_name} WHERE ticker = '{ticker}' ORDER BY date DESC LIMIT 1"
    postgres.run_query(stocks_database.cursor, query)
    try:
        price = postgres.get_list_results(stocks_database.cursor)[0]
        return price
    except:
        return None


create()
