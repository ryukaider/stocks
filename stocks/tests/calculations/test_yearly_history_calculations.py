import pytest
from calculations import yearly_history_calculations


@pytest.mark.skip()
def test_calculate_end_of_year_price():
    yearly_history_calculations.calculate_end_of_year_price()


@pytest.mark.skip()
def test_calculate_average_price():
    yearly_history_calculations.calculate_average_price()


@pytest.mark.skip()
def test_calculate_dividend():
    yearly_history_calculations.calculate_dividend()


@pytest.mark.skip()
def test_calculate_dividend_yield():
    yearly_history_calculations.calculate_dividend_yield()
