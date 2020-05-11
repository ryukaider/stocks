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
    stocks = []
    stocks.append(create_random_stock())
    stocks.append(create_random_stock())
    assert tickers_table.add_stocks(stocks) is True
    assert tickers_table.remove_stocks(stocks) is True


def test_get_tickers():
    assert tickers_table.get_tickers() is not None


def create_random_stock():
    stock = Stock()
    stock.ticker = random_utilities.random_letters(4)
    stock.exchange = random_utilities.random_letters(6)
    stock.name = random_utilities.random_letters(8)
    return stock
