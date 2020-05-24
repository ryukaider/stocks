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


def test_calculate_average_price():
    average_price = yearly_history_calculations.calculate_average_price('MSFT', 2019)
    assert average_price > 0


def test_calculate_average_prices():
    average_prices = yearly_history_calculations.calculate_average_prices('MSFT')
    assert len(average_prices) >= 20
    for year, price in average_prices.items():
        assert year >= 2000
        assert price > 0


def test_calculate_dividend():
    dividend = yearly_history_calculations.calculate_dividend('MSFT', 2019)
    assert dividend == 1.89


def test_calculate_dividends():
    dividends = yearly_history_calculations.calculate_dividends('MSFT')
    assert len(dividends) >= 20
    for year, dividend in dividends.items():
        assert year >= 2000
        assert dividend >= 0


@pytest.mark.skip()
def test_calculate_dividend_decimal():
    yearly_history_calculations.calculate_dividend()


@pytest.mark.skip()
def test_calculate_dividend_yields():
    dividend_yields = yearly_history_calculations.calculate_average_dividend_yields('MSFT')
    assert len(dividend_yields) >= 20
    for year, dividend_yield in dividend_yields.items():
        assert year >= 2000
        assert dividend_yield >= 0


@pytest.mark.skip()
def test_calculate_dividend_yields_zero():
    pass
