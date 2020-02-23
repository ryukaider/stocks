import sys
sys.path.append('E:/Google Drive/Computers/Dev/Stocks/scott_stocks')

from database import postgres
from database import stocks_database

table = 'yearly_history'

def update_end_price(ticker, year, price):
    if not postgres.insert_row(stocks_database.cursor, table, '(ticker,year,end_price)', f"('{ticker}',{year},{price})"):
        update_query = f"UPDATE {table} SET end_price = {price} WHERE ticker = '{ticker}' AND year = {year}"
        postgres.run_query(stocks_database.cursor, update_query)

def update_average_price(ticker, year, price):
    if not postgres.insert_row(stocks_database.cursor, table, '(ticker,year,average_price)', f"('{ticker}',{year},{price})"):
        update_query = f"UPDATE {table} SET average_price = {price} WHERE ticker = '{ticker}' AND year = {year}"
        postgres.run_query(stocks_database.cursor, update_query)

def update_dividend(ticker, year, dividend):
    if not postgres.insert_row(stocks_database.cursor, table, '(ticker,year,dividend)', f"('{ticker}',{year},{dividend})"):
        update_query = f"UPDATE {table} SET dividend = {dividend} WHERE ticker = '{ticker}' AND year = {year}"
        postgres.run_query(stocks_database.cursor, update_query)

def update_dividend_yield(ticker, year, dividend_yield):
    if not postgres.insert_row(stocks_database.cursor, table, '(ticker,year,dividend_yield)', f"('{ticker}',{year},{dividend_yield})"):
        update_query = f"UPDATE {table} SET dividend_yield = {dividend_yield} WHERE ticker = '{ticker}' AND year = {year}"
        postgres.run_query(stocks_database.cursor, update_query)

def get_data(ticker):
    query = f"SELECT * FROM {table} WHERE ticker = '{ticker}' ORDER BY year DESC"
    postgres.run_query(stocks_database.cursor, query)
    data = stocks_database.cursor.fetchall()
    return data

if __name__ == "__main__":
    update_dividend('MSFT', 2019, 0)
