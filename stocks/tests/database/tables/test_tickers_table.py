import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(_root_path)

import pytest
from database.tables.tickers_table import TickersTable
from stock import Stock
from utilities import random_utilities

table_name = 'testtickerstable'
table = TickersTable(table_name)


def test_exists():
    assert table.exists() is True


def test_create():
    assert table.create() is True


def test_add_remove_stock():
    stock = create_random_stock()
    assert table.add_stock(stock) is True
    assert table.remove_stock(stock) is True


def test_add_remove_stocks():
    stocks = []
    stocks.append(create_random_stock())
    stocks.append(create_random_stock())
    assert table.add_stocks(stocks) is True
    assert table.remove_stocks(stocks) is True


def test_get_tickers():
    assert table.get_tickers() is not None


def create_random_stock():
    stock = Stock()
    stock.ticker = random_utilities.random_letters(4)
    stock.exchange = random_utilities.random_letters(6)
    stock.name = random_utilities.random_letters(8)
    return stock
