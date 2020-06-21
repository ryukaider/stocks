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


def test_add_rows():
    rows = [_random_row(), _random_row()]
    assert daily_history_table.add_rows(rows) is True
    retrieved_row1 = daily_history_table.get_history(rows[0]['ticker'], rows[0]['date'].year)
    assert len(retrieved_row1) == 1
    retrieved_row2 = daily_history_table.get_history(rows[1]['ticker'], rows[1]['date'].year)
    assert len(retrieved_row2) == 1


def test_update_row():
    row = _random_row()
    daily_history_table.add_rows([row])

    updated_row = row
    dividend = random_utilities.random_double()
    updated_row['dividend'] = dividend
    assert daily_history_table.update_row(row) is True

    retrieved_rows = daily_history_table.get_history(row['ticker'], row['date'].year)
    retrieved_row = retrieved_rows[0]
    assert float(retrieved_row['dividend']) == dividend
    assert float(retrieved_row['adjusted_close']) == row['adjusted_close']


def test_upsert_row():
    row = _random_row()

    retrieved_rows = daily_history_table.get_history(row['ticker'])
    assert len(retrieved_rows) == 0

    assert daily_history_table.upsert_row(row) is True
    retrieved_row = daily_history_table.get_history(row['ticker'])[0]
    assert float(retrieved_row['dividend']) == row['dividend']

    row['dividend'] = random_utilities.random_double()
    assert daily_history_table.upsert_row(row) is True
    retrieved_row = daily_history_table.get_history(row['ticker'])[0]
    assert float(retrieved_row['dividend']) == row['dividend']


def test_get_history():
    rows = [_random_row(test_ticker)]
    daily_history_table.add_rows(rows)
    history = daily_history_table.get_history(test_ticker)
    assert history is not None
    assert len(history) >= 0


def test_get_history_desc():
    pass


def test_get_history_invalid():
    pass


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
