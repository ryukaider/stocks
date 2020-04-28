import os, sys
root_path = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(root_path)

import pytest
from calculation_to_database import calculations_to_current_data


@pytest.mark.skip()
def test_update_all():
    calculations_to_current_data.update_all()


@pytest.mark.skip()
def test_update_all_latest_price():
    calculations_to_current_data.update_all_latest_price()


@pytest.mark.skip()
def test_update_latest_price():
    calculations_to_current_data.update_latest_price()


@pytest.mark.skip()
def test_update_all_rolling_annual_dividend():
    calculations_to_current_data.update_all_dividend_ttm()


@pytest.mark.skip()
def test_update_rolling_annual_dividend():
    calculations_to_current_data.update_dividend_ttm()


@pytest.mark.skip()
def test_update_all_dividend_yield():
    calculations_to_current_data.update_all_dividend_yield()
    

@pytest.mark.skip()
def test_update_dividend_yield():
    calculations_to_current_data.update_dividend_yield()


@pytest.mark.skip()
def test_update_all_dividend_years():
    calculations_to_current_data.update_all_dividend_years()
    

@pytest.mark.skip()
def test_update_dividend_years():
    calculations_to_current_data.update_dividend_years()


@pytest.mark.skip()
def test_update_all_dividend_years_increasing():
    calculations_to_current_data.update_all_dividend_years_increasing()
    

@pytest.mark.skip()
def test_update_dividend_years_increasing():
    calculations_to_current_data.update_dividend_years_increasing()


@pytest.mark.skip()
def test_update_all_payout_ratio_ttm():
    calculations_to_current_data.update_all_payout_ratio_ttm()


@pytest.mark.skip()
def test_update_payout_ratio_ttm():
    calculations_to_current_data.update_payout_ratio_ttm()
