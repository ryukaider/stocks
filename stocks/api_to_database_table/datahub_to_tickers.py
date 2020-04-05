import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(_root_path)

from web_apis import datahub
from database.tables import tickers_table


def add_tickers():
    stocks = datahub.get_all_stocks_ticker_name_exchange()
    tickers_table.add_stocks(stocks)


if __name__ == "__main__":
    add_tickers()
