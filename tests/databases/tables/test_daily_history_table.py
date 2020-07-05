import pytest
from config import database_config
from database.database import Database
from database.tables.daily_history_table import DailyHistoryTable
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


def test_upsert_1row():
    rows = [_random_row()]

    retrieved_rows = daily_history_table.get_history(rows[0]['ticker'])
    assert len(retrieved_rows) == 0

    assert daily_history_table.upsert(rows) is True
    retrieved_row = daily_history_table.get_history(rows[0]['ticker'])[0]
    assert float(retrieved_row['dividend']) == rows[0]['dividend']

    rows[0]['dividend'] = random_utilities.random_double()
    assert daily_history_table.upsert(rows) is True
    retrieved_row = daily_history_table.get_history(rows[0]['ticker'])[0]
    assert float(retrieved_row['dividend']) == rows[0]['dividend']


def test_upsert_rows_none():
    assert daily_history_table.upsert(None) is False


@pytest.mark.skip
def test_upsert_2rows():
    pass


@pytest.mark.skip
def test_get_history_desc():
    pass


@pytest.mark.skip
def test_get_history_invalid():
    pass


@pytest.mark.skip
def test_get_history_by_year():
    pass


def _random_row(ticker=None):
    if ticker is None:
        ticker = random_utilities.random_letters()
    return {
        'ticker': ticker,
        'date': random_utilities.random_date(),
        'open': random_utilities.random_double(),
        'high': random_utilities.random_double(),
        'low': random_utilities.random_double(),
        'close': random_utilities.random_double(),
        'adjusted_close': random_utilities.random_double(),
        'volume': random_utilities.random_int(0, 10000000),
        'dividend': random_utilities.random_double(),
        'split_coefficient': 1.000
    }
