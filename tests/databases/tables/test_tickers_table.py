from config import database_config
from database.database import Database
from database.tables.tickers_table import TickersTable
from utilities import random_utilities

db = Database(database_config.test_database)
tickers_table = TickersTable(db.cursor())


def test_exists():
    assert tickers_table.exists() is True


def test_create():
    assert tickers_table.create() is True


def test_add_tickers():
    tickers = []
    for _ in range(1, 3):
        tickers.append(random_utilities.random_letters())
    assert tickers_table.add_tickers(tickers) is True


def test_add_tickers_one_duplicate():
    new_ticker = random_utilities.random_letters()
    tickers_table.add_ticker('test')
    tickers = ['test', new_ticker]
    assert tickers_table.add_tickers(tickers) is True
    retrieved_tickers = tickers_table.get_tickers()
    assert new_ticker in retrieved_tickers


def test_add_remove_ticker():
    ticker = random_utilities.random_letters()
    assert tickers_table.add_ticker(ticker) is True
    assert tickers_table.remove_ticker(ticker) is True


def test_add_remove_stocks():
    tickers = [random_utilities.random_letters(), random_utilities.random_letters()]
    assert tickers_table.add_tickers(tickers) is True
    assert tickers_table.remove_tickers(tickers) is True


def test_get_tickers():
    ticker = random_utilities.random_letters()
    tickers_table.add_ticker(ticker)
    tickers = tickers_table.get_tickers()
    assert tickers is not None
    assert len(tickers) > 0
    assert ticker in tickers
    for ticker in tickers:
        assert isinstance(ticker, str)
        assert len(ticker) > 0
