import pytest
from database.stocks_database import StocksDatabase
from database_updaters.yearly_history.yearly_history_calculator import YearlyHistoryCalculator

# Uses data from the real database
yearly_history_calculator = YearlyHistoryCalculator(StocksDatabase())


def test_calculate_end_of_year_price():
    price = yearly_history_calculator.calculate_end_of_year_price('MSFT', 2019)
    assert price > 0


def test_calculate_end_of_year_price_no_history():
    price = yearly_history_calculator.calculate_end_of_year_price('AA', 2000)
    assert price is None


def test_calculate_end_of_year_prices():
    prices = yearly_history_calculator.calculate_end_of_year_prices('MSFT')
    assert len(prices) >= 20
    for year, price in prices.items():
        assert year >= 2000
        assert price > 0


def test_calculate_average_price():
    average_price = yearly_history_calculator.calculate_average_price('MSFT', 2019)
    assert average_price > 0


def test_calculate_average_price_no_rows():
    average_price = yearly_history_calculator.calculate_average_price('AA', 2000)
    assert average_price is None


def test_calculate_average_prices():
    average_prices = yearly_history_calculator.calculate_average_prices('MSFT')
    assert len(average_prices) >= 20
    for year, price in average_prices.items():
        assert year >= 2000
        assert price > 0


def test_calculate_dividend():
    dividend = yearly_history_calculator.calculate_dividend('MSFT', 2019)
    assert dividend == 1.89


def test_calculate_dividends():
    dividends = yearly_history_calculator.calculate_dividends('MSFT')
    assert len(dividends) >= 20
    for year, dividend in dividends.items():
        assert year >= 2000
        assert dividend >= 0


@pytest.mark.skip()
def test_calculate_dividend_decimal():
    yearly_history_calculator.calculate_dividend()


@pytest.mark.skip()
def test_calculate_dividend_yields():
    dividend_yields = yearly_history_calculator.calculate_average_dividend_yields('MSFT')
    assert len(dividend_yields) >= 20
    for year, dividend_yield in dividend_yields.items():
        assert year >= 2000
        assert dividend_yield >= 0


@pytest.mark.skip()
def test_calculate_dividend_yields_zero():
    pass
