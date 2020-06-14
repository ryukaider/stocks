import pytest
from config import database_config
from databases.database import Database
from databases.tables.api_progress_table import ApiProgressTable
from utilities import random_utilities

db = Database(database_config.test_database)
cursor = db.cursor()

table_name = 'test_api_progress'
api_progress_table = ApiProgressTable(cursor, table_name)

test_ticker = 'TEST'


def test_exists():
    assert api_progress_table.exists()


def test_create():
    assert api_progress_table.create()


def test_add_tickers():
    tickers = []
    for _ in range(1, 3):
        tickers.append(random_utilities.random_letters())
    assert api_progress_table.add_tickers(tickers) is True


def test_add_tickers_one_duplicate():
    new_ticker = random_utilities.random_letters()
    api_progress_table.add_ticker('test')
    tickers = ['test', new_ticker]
    assert api_progress_table.add_tickers(tickers) is True


def test_add_stock():
    ticker = random_utilities.random_letters(12)
    assert api_progress_table.add_ticker(ticker) is True


def test_add_stock_duplicate():
    ticker = 'duplicate'
    api_progress_table.add_ticker(ticker)
    assert api_progress_table.add_ticker(ticker) is False


def test_add_stock_no_ticker():
    with pytest.raises(Exception):
        api_progress_table.add_ticker()


def test_update_daily_history_progress():
    api_progress_table.add_ticker(test_ticker)
    date = random_utilities.random_date()
    assert api_progress_table.update_daily_history_progress(test_ticker, date) is True
    retrieved_date = api_progress_table.get_value('ticker', test_ticker, 'daily_history')
    assert retrieved_date == date


def test_reset_daily_history_progress():
    api_progress_table.add_ticker(test_ticker)
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


def test_update_company_profile_progress():
    api_progress_table.add_ticker(test_ticker)
    date = random_utilities.random_date()
    assert api_progress_table.update_company_profile_progress(test_ticker, date) is True
    retrieved_date = api_progress_table.get_value('ticker', test_ticker, 'company_profile')
    assert retrieved_date == date


def test_reset_company_profile_progress():
    api_progress_table.add_ticker(test_ticker)
    date = random_utilities.random_date()
    api_progress_table.update_company_profile_progress(test_ticker, date)
    assert api_progress_table.reset_company_profile_progress(test_ticker) is True
    retrieved_date = api_progress_table.get_value('ticker', test_ticker, 'company_profile')
    assert retrieved_date is None


def test_get_company_profile_progress():
    add_random_row()
    results = api_progress_table.get_company_profile_progress()
    assert len(results) > 0
    for ticker in results:
        assert isinstance(ticker, str)


@pytest.mark.skip()
def test_get_daily_history_progress_null():
    pass


@pytest.mark.skip()
def test_get_progress_asc():
    pass


@pytest.mark.skip()
def test_get_progress_nulls_first():
    pass


def add_random_row():
    row = {
        'ticker': random_utilities.random_letters(),
        'company_profile': random_utilities.random_date(),
        'daily_history': random_utilities.random_date()
    }
    api_progress_table.insert_row(row)
