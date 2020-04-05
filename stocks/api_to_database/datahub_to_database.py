import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(_root_path)

from database import postgres
from database import stocks_database

from web_apis import datahub
from database.tables import tickers_table

def add_tickers(table = 'tickers'):
    stocks = datahub.get_all_stocks_ticker_name_exchange()
    tickers_table.add_tickers(stocks, table)

if __name__ == "__main__":
    add_tickers()
