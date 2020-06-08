from config import database_config
from databases.database import Database
from databases.tables.tickers_table import TickersTable
from utilities import random_utilities

database_name = database_config.test_database
table_name = 'test_tickers'
db = Database(database_name)
cursor = db.cursor()
tickers_table = TickersTable(cursor, table_name)


def test_exists():
    assert tickers_table.exists() is True


def test_create():
    assert tickers_table.create() is True


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
