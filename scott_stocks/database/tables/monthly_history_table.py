from database import postgres
from database import stocks_database

table = 'monthly_history'

def add_monthly_data(monthly_data):
    for row in monthly_data:
        add_monthly_row(row)

def add_monthly_row(monthly_row):
    if not postgres.insert_row(stocks_database.cursor, table, '(ticker, date, price, dividend)',
        f"('{monthly_row['ticker']}','{monthly_row['date']}','{monthly_row['price']}','{monthly_row['dividend']}')"):
        update_query = f"UPDATE {table} SET price = '{monthly_row['price']}' WHERE ticker = '{monthly_row['ticker']}' AND date = '{monthly_row['date']}'"
        postgres.run_query(stocks_database.cursor, update_query)

def get_history(ticker):
    query = f"SELECT * FROM {table} WHERE ticker = '{ticker}' ORDER BY date DESC"
    postgres.run_query(stocks_database.cursor, query)
    data = stocks_database.cursor.fetchall()
    return data

def get_date_dividend(ticker):
    query = f"SELECT date,dividend FROM {table} WHERE ticker = '{ticker}' ORDER BY date DESC"
    postgres.run_query(stocks_database.cursor, query)
    data = stocks_database.cursor.fetchall()
    return data

def get_dividend_ttm(ticker):
    query = f"SELECT dividend FROM {table} WHERE ticker = '{ticker}' ORDER BY date DESC LIMIT 12"
    postgres.run_query(stocks_database.cursor, query)
    dividends = postgres.get_list_results(stocks_database.cursor)
    return dividends

def get_latest_price(ticker):
    query = f"SELECT price FROM {table} WHERE ticker = '{ticker}' ORDER BY date DESC LIMIT 1"
    postgres.run_query(stocks_database.cursor, query)
    try:
        price = postgres.get_list_results(stocks_database.cursor)[0]
        return price
    except:
        return None
