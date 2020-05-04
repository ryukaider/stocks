from database.tables.tickers_table import TickersTable
from web_apis import datahub

tickers_table = TickersTable()


def add_tickers():
    stocks = datahub.get_all_stocks_ticker_name_exchange()
    tickers_table.add_stocks(stocks)


if __name__ == "__main__":
    add_tickers()
