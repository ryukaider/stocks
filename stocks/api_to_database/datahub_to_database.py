import sys
sys.path.append('E:/Google Drive/Computers/Dev/Stocks/scott_stocks')

from web_apis import datahub
from database.tables import tickers_table

def add_tickers(table = 'tickers'):
    stocks = datahub.get_all_stocks_ticker_name_exchange()
    tickers_table.add_tickers(stocks, table)

if __name__ == "__main__":
    add_tickers()
