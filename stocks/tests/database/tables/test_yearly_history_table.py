import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(_root_path)

import pytest
from utilities import random_utilities
from database.tables.yearly_history_table import YearlyHistoryTable

table_name = 'test_yearly_history'
test_ticker = 'TEST'
test_year = 2020

yearly_history_table = YearlyHistoryTable(table_name)


def test_exists():
    assert yearly_history_table.exists()


def test_create():
    assert yearly_history_table.create()


def test_update_end_price():
    end_price = random_utilities.random_double()
    yearly_history_table.update_end_price(test_ticker, test_year, end_price)


def test_update_average_price():
    average_price = random_utilities.random_double()
    yearly_history_table.update_average_price(test_ticker, test_year, average_price)


def test_update_dividend():
    dividend = random_utilities.random_double()
    yearly_history_table.update_dividend(test_ticker, test_year, dividend)


def test_update_dividend_yield():
    dividend_yield = random_utilities.random_double()
    yearly_history_table.update_dividend_yield(test_ticker, test_year, dividend_yield)


def test_get_data():
    data = yearly_history_table.get_data(test_ticker)
    assert data is not None
