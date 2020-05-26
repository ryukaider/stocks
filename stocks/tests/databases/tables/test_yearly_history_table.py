import pytest
from config import database_config
from databases.tables.yearly_history_table import YearlyHistoryTable
from utilities import random_utilities

database_name = database_config.test_database
table_name = 'test_yearly_history'
test_ticker = 'TEST'
test_year = 2020

yearly_history_table = YearlyHistoryTable(table_name, database_name)


def test_exists():
    assert yearly_history_table.exists()


def test_create():
    assert yearly_history_table.create()


def test_update_end_price():
    end_price = random_utilities.random_double()
    assert yearly_history_table.update_end_price(test_ticker, test_year, end_price) is True


def test_update_end_price_none_price():
    assert yearly_history_table.update_end_price(test_ticker, test_year, None) is True


def test_update_average_price():
    average_price = random_utilities.random_double()
    yearly_history_table.update_average_price(test_ticker, test_year, average_price)
    retrieved_average_price = yearly_history_table.get_average_price(test_ticker, test_year)
    assert retrieved_average_price == average_price


def test_update_dividend():
    dividend = random_utilities.random_double()
    yearly_history_table.update_dividend(test_ticker, test_year, dividend)
    retrieved_dividend = yearly_history_table.get_dividend(test_ticker, test_year)
    assert retrieved_dividend == dividend


def test_update_dividend_yield():
    dividend_yield = random_utilities.random_double()
    yearly_history_table.update_dividend_yield(test_ticker, test_year, dividend_yield)


@pytest.mark.skip
def test_get_value():
    pass


def test_get_data():
    data = yearly_history_table.get_data(test_ticker)
    assert data is not None


@pytest.mark.skip
def test_row_exists():
    pass


def test_row_exists_doesnt_exist():
    ticker = random_utilities.random_letters()
    year = random_utilities.random_date().year
    assert yearly_history_table.row_exists(ticker, year) is False
