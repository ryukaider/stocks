import pytest
from calculations import yearly_history_calculations


def test_calculate_end_of_year_price():
    price = yearly_history_calculations.calculate_end_of_year_price('MSFT', 2019)
    assert price > 0


def test_calculate_end_of_year_prices():
    prices = yearly_history_calculations.calculate_end_of_year_prices('MSFT')
    assert len(prices) >= 20
    for year, price in prices.items():
        assert year >= 2000
        assert price > 0


@pytest.mark.skip()
def test_calculate_average_price():
    yearly_history_calculations.calculate_average_price()


@pytest.mark.skip()
def test_calculate_dividend():
    yearly_history_calculations.calculate_dividend()


@pytest.mark.skip()
def test_calculate_dividend_yield():
    yearly_history_calculations.calculate_dividend_yield()
