import pytest
from database_updaters.calculations import current_data_calculations


@pytest.mark.skip()
def test_calculate_dividend_ttm():
    current_data_calculations.calculate_dividend_ttm()


@pytest.mark.skip()
def test_calculate_dividend_yield():
    current_data_calculations.calculate_dividend_yield()


@pytest.mark.skip()
def test_calculate_years_of_dividends():
    current_data_calculations.calculate_years_of_dividends()


@pytest.mark.skip()
def test_calculate_years_of_dividends_increasing():
    current_data_calculations.calculate_years_of_dividends_increasing()


@pytest.mark.skip()
def test_calculate_payout_ratio_ttm():
    current_data_calculations.calculate_payout_ratio_ttm()
