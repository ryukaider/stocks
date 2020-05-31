from config import database_config
from databases.tables.tickers_table import TickersTable
from stock import Stock
from utilities import random_utilities

database_name = database_config.test_database
table_name = 'test_tickers'
tickers_table = TickersTable(table_name, database_name)


def test_exists():
    assert tickers_table.exists() is True


def test_create():
    assert tickers_table.create() is True


def test_add_remove_stock():
    stock = create_random_stock()
    assert tickers_table.add_stock(stock) is True
    assert tickers_table.remove_stock(stock) is True


def test_add_remove_stocks():
    stocks = [create_random_stock(), create_random_stock()]
    assert tickers_table.add_stocks(stocks) is True
    assert tickers_table.remove_stocks(stocks) is True


def test_get_tickers():
    stock = create_random_stock()
    tickers_table.add_stock(stock)
    tickers = tickers_table.get_tickers()
    assert tickers is not None
    assert len(tickers) > 0
    for ticker in tickers:
        assert isinstance(ticker, str)
        assert len(ticker) > 0


def create_random_stock():
    stock = Stock()
    stock.ticker = random_utilities.random_letters(4)
    stock.exchange = random_utilities.random_letters(6)
    stock.name = random_utilities.random_letters(8)
    return stock
