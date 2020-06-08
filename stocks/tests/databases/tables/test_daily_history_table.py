from config import database_config
from databases.database import Database
from databases.tables.daily_history_table import DailyHistoryTable
from utilities import random_utilities

database_name = database_config.test_database
table_name = 'test_daily_history'
test_ticker = 'TEST'
db = Database(database_name)
cursor = db.cursor()
daily_history_table = DailyHistoryTable(cursor, table_name)


def test_exists():
    assert daily_history_table.exists()


def test_create():
    assert daily_history_table.create()


def test_add_row():
    row = {
        'ticker': random_utilities.random_string(),
        'date': '2020-04-25',
        'close': random_utilities.random_double(),
        'dividend': random_utilities.random_double()
    }
    assert daily_history_table.add_row(row) is True


def test_get_history():
    row = {
        'ticker': test_ticker,
        'date': '2020-04-25',
        'close': random_utilities.random_double(),
        'dividend': random_utilities.random_double()
    }
    daily_history_table.add_row(row)
    history = daily_history_table.get_history(test_ticker)
    assert history is not None
    assert len(history) >= 0


def test_get_history_desc():
    pass


def test_get_history_invalid():
    pass


def test_get_history_by_year():
    pass
