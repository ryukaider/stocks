import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(_root_path)

import pytest
from database.tables.current_data_table import CurrentDataTable
from utilities import random_utilities

table_name = 'test_current_data'
test_ticker = 'test'
current_data_table = CurrentDataTable(table_name)


@pytest.fixture(autouse=True, scope="class")
def setup_once_per_class():
    current_data_table.add_stock(test_ticker)


def test_exists():
    assert current_data_table.exists()


def test_create():
    assert current_data_table.create()


def test_add_stock():
    ticker = random_utilities.random_letters(12)
    assert current_data_table.add_stock(ticker)


def test_name():
    name = random_utilities.random_letters(12)
    assert current_data_table.update_name(test_ticker, name)
    retrieved_name = current_data_table.get_name(test_ticker)
    assert retrieved_name == name


def test_exchange():
    exchange = random_utilities.random_letters(8)
    assert current_data_table.update_exchange(test_ticker, exchange)
    retrieved_exchange = current_data_table.get_exchange(test_ticker)
    assert retrieved_exchange == exchange


def test_price():
    price = random_utilities.random_double()
    assert current_data_table.update_price(test_ticker, price)
    retrieved_price = current_data_table.get_price(test_ticker)
    assert retrieved_price == price


def test_dividend_ttm():
    dividend_ttm = random_utilities.random_double()
    assert current_data_table.update_dividend_ttm(test_ticker, dividend_ttm)
    retrieved_dividend_ttm = current_data_table.get_dividend_ttm(test_ticker)
    assert retrieved_dividend_ttm == dividend_ttm


def test_dividend_yield():
    dividend_yield = random_utilities.random_double()
    assert current_data_table.update_dividend_yield(test_ticker, dividend_yield)
    retrieved_dividend_yield = current_data_table.get_dividend_yield(test_ticker)
    assert retrieved_dividend_yield == dividend_yield


def test_dividend_years():
    dividend_years = random_utilities.random_int()
    assert current_data_table.update_dividend_years(test_ticker, dividend_years)
    retrieved_dividend_years = current_data_table.get_dividend_years(test_ticker)
    assert retrieved_dividend_years == dividend_years


def test_dividend_years_increasing():
    dividend_years_increasing = random_utilities.random_int()
    assert current_data_table.update_dividend_years_increasing(test_ticker, dividend_years_increasing)
    retrieved_dividend_years_increasing = current_data_table.get_dividend_years_increasing(test_ticker)
    assert retrieved_dividend_years_increasing == dividend_years_increasing


def test_payout_ratio_ttm():
    payout_ratio_ttm = random_utilities.random_double()
    assert current_data_table.update_payout_ratio_ttm(test_ticker, payout_ratio_ttm)
    retrieved_payout_ratio_ttm = current_data_table.get_payout_ratio_ttm(test_ticker)
    assert retrieved_payout_ratio_ttm == payout_ratio_ttm


def test_eps_ttm():
    eps_ttm = random_utilities.random_double()
    assert current_data_table.update_eps_ttm(test_ticker, eps_ttm)
    retrieved_eps_ttm = current_data_table.get_eps_ttm(test_ticker)
    assert retrieved_eps_ttm == eps_ttm
