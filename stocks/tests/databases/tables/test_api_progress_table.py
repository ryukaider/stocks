import pytest
from databases.tables.api_progress_table import ApiProgressTable
from utilities import random_utilities

table_name = 'test_api_progress'
test_ticker = 'test'
api_progress_table = ApiProgressTable(table_name)


def test_exists():
    assert api_progress_table.exists()


def test_create():
    assert api_progress_table.create()


@pytest.mark.skip('slow test')
def test_reset_all():
    api_progress_table.reset_all()


def test_add_stock():
    ticker = random_utilities.random_letters(12)
    assert api_progress_table.add_stock(ticker)


def test_add_stock_duplicate():
    ticker = 'duplicate'
    api_progress_table.add_stock(ticker)
    assert api_progress_table.add_stock(ticker) is False


def test_add_stock_no_ticker():
    with pytest.raises(Exception):
        api_progress_table.add_stock()


def test_reset_monthly_progress():
    api_progress_table.add_stock(test_ticker)
    assert api_progress_table.reset_monthly_progress(test_ticker)


def test_reset_monthly_progress_no_ticker():
    with pytest.raises(Exception):
        api_progress_table.reset_monthly_progress()


def test_set_monthly_done_no_ticker():
    assert api_progress_table.set_monthly_done(test_ticker)


def test_set_monthly_done_no_ticker():
    with pytest.raises(Exception):
        api_progress_table.set_monthly_done()


def test_reset_eps_progress():
    assert api_progress_table.reset_eps_progress(test_ticker)


def test_reset_eps_progress_no_ticker():
    with pytest.raises(Exception):
        api_progress_table.reset_eps_progress()


def test_set_eps_done():
    assert api_progress_table.set_eps_done(test_ticker)


def test_set_eps_done_no_ticker():
    with pytest.raises(Exception):
        api_progress_table.set_eps_done()


def test_get_incomplete_stocks_monthly():
    stocks = api_progress_table.get_incomplete_stocks('monthly')
    assert len(stocks) > 0


def test_get_incomplete_stocks_eps():
    stocks = api_progress_table.get_incomplete_stocks('eps')
    assert len(stocks) > 0


def test_get_incomplete_stocks_invalid():
    with pytest.raises(Exception):
        api_progress_table.get_incomplete_stocks('invalid')
