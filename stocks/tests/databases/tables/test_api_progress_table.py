import pytest
from config import database_config
from databases.tables.api_progress_table import ApiProgressTable
from utilities import random_utilities

database_name = database_config.test_database
table_name = 'test_api_progress'
test_ticker = 'TEST'
api_progress_table = ApiProgressTable(table_name, database_name)


def test_exists():
    assert api_progress_table.exists()


def test_create():
    assert api_progress_table.create()


@pytest.mark.skip('slow test')
def test_reset_all():
    api_progress_table.reset_all()


def test_add_stock():
    ticker = random_utilities.random_letters(12)
    assert api_progress_table.add_stock(ticker) is True


def test_add_stock_duplicate():
    ticker = 'duplicate'
    api_progress_table.add_stock(ticker)
    assert api_progress_table.add_stock(ticker) is False


def test_add_stock_no_ticker():
    with pytest.raises(Exception):
        api_progress_table.add_stock()


def test_update_daily_history_progress():
    api_progress_table.add_stock(test_ticker)
    date = random_utilities.random_date()
    assert api_progress_table.update_daily_history_progress(test_ticker, date) is True
    retrieved_date = api_progress_table.get_value('ticker', test_ticker, 'daily_history')
    assert retrieved_date == date


def test_reset_daily_history_progress():
    api_progress_table.add_stock(test_ticker)
    date = random_utilities.random_date()
    api_progress_table.update_daily_history_progress(test_ticker, date)
    assert api_progress_table.reset_daily_history_progress(test_ticker) is True
    retrieved_date = api_progress_table.get_value('ticker', test_ticker, 'daily_history')
    assert retrieved_date is None


def test_get_daily_history_progress():
    add_random_row()
    results = api_progress_table.get_daily_history_progress()
    assert len(results) > 0
    for ticker in results:
        assert isinstance(ticker, str)


@pytest.mark.skip()
def test_get_daily_history_progress_null():
    pass


def add_random_row():
    row = {
        'ticker': random_utilities.random_letters(),
        'daily_history': random_utilities.random_date()
    }
    api_progress_table.insert_row(row)
