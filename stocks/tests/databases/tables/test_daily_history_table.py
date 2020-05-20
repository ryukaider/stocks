from config import database_config
from databases.tables.daily_history_table import DailyHistoryTable
from utilities import random_utilities

database_name = database_config.test_database
table_name = 'test_daily_history'
test_ticker = 'TEST'
daily_history_table = DailyHistoryTable(table_name, database_name)


def test_exists():
    assert daily_history_table.exists()


def test_create():
    assert daily_history_table.create()


def test_add_row():
    row = {
        'ticker': random_utilities.random_string(),
        'date': '2020-04-25',
        'price': random_utilities.random_double(),
        'dividend': random_utilities.random_double()
    }
    assert daily_history_table.add_row(row) is True
