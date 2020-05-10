import pytest
from utilities import random_utilities
from databases.tables.monthly_history_table import MonthlyHistoryTable

table_name = 'test_monthly_history'
test_ticker = 'TEST'
monthly_history_table = MonthlyHistoryTable(table_name)

monthly_history_table.add_monthly_row({
        'ticker': test_ticker,
        'date': '2020-04-25',
        'price': random_utilities.random_double(),
        'dividend': random_utilities.random_double()
    })


def test_exists():
    assert monthly_history_table.exists()


def test_create():
    assert monthly_history_table.create()


@pytest.mark.skip()
def test_add_monthly_data():
    monthly_history_table.add_monthly_data()


def test_add_monthly_row():
    monthly_row = {
        'ticker': random_utilities.random_letters(8),
        'date': '2020-04-25',
        'price': random_utilities.random_double(),
        'dividend': random_utilities.random_double()
    }
    monthly_history_table.add_monthly_row(monthly_row)


def test_get_history():
    history = monthly_history_table.get_history(test_ticker)
    assert history is not None


def test_get_date_dividend():
    history = monthly_history_table.get_date_dividend(test_ticker)
    assert history is not None


def test_get_dividend_ttm():
    data = monthly_history_table.get_dividend_ttm(test_ticker)
    assert data is not None


def test_get_latest_price():
    price = monthly_history_table.get_latest_price(test_ticker)
    assert price is not None
