import pytest
from calculation_to_database import calculations_to_yearly_history


@pytest.mark.skip()
def test_update_all():
    calculations_to_yearly_history.update_all_stocks()


@pytest.mark.skip()
def test_update_end_of_year_price():
    calculations_to_yearly_history.update_end_price()


@pytest.mark.skip()
def test_update_average_price():
    calculations_to_yearly_history.update_average_price()


@pytest.mark.skip()
def test_update_annual_dividends():
    calculations_to_yearly_history.update_annual_dividends()


@pytest.mark.skip()
def test_update_dividend_yields():
    calculations_to_yearly_history.update_dividend_yields()
