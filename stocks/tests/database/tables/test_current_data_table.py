import pytest
from database.tables.current_data_table import CurrentDataTable
from utilities import random_utilities

table_name = 'test_current_data'
test_ticker = 'TEST'
current_data_table = CurrentDataTable(table_name)


@pytest.fixture(autouse=True, scope="class")
def setup_once_per_class():
    current_data_table.add_stock(test_ticker)


def test_exists():
    assert current_data_table.exists()


def test_create():
    assert current_data_table.create()


def test_add_stock():
    ticker = random_utilities.random_letters(12)
    assert current_data_table.add_stock(ticker)


def test_name():
    name = random_utilities.random_letters(12)
    assert current_data_table.update_name(test_ticker, name)
    retrieved_name = current_data_table.get_name(test_ticker)
    assert retrieved_name == name


def test_exchange():
    exchange = random_utilities.random_letters(8)
    assert current_data_table.update_exchange(test_ticker, exchange)
    retrieved_exchange = current_data_table.get_exchange(test_ticker)
    assert retrieved_exchange == exchange


def test_sector():
    sector = random_utilities.random_letters(8)
    assert current_data_table.update_sector(test_ticker, sector)
    retrieved_sector = current_data_table.get_sector(test_ticker)
    assert retrieved_sector == sector


def test_industry():
    industry = random_utilities.random_letters(8)
    assert current_data_table.update_industry(test_ticker, industry)
    retrieved_industry = current_data_table.get_industry(test_ticker)
    assert retrieved_industry == industry


def test_ceo():
    ceo = random_utilities.random_letters(8)
    assert current_data_table.update_ceo(test_ticker, ceo)
    retrieved_ceo = current_data_table.get_ceo(test_ticker)
    assert retrieved_ceo == ceo


def test_website():
    website = random_utilities.random_letters(8)
    assert current_data_table.update_website(test_ticker, website)
    retrieved_website = current_data_table.get_website(test_ticker)
    assert retrieved_website == website


def test_description():
    description = random_utilities.random_letters(8)
    assert current_data_table.update_description(test_ticker, description)
    retrieved_description = current_data_table.get_description(test_ticker)
    assert retrieved_description == description


def test_price():
    price = random_utilities.random_double()
    assert current_data_table.update_price(test_ticker, price)
    retrieved_price = current_data_table.get_price(test_ticker)
    assert retrieved_price == price


def test_update_price_none():
    assert current_data_table.update_price(test_ticker, price=None) is False


def test_change():
    change = random_utilities.random_double()
    assert current_data_table.update_change(test_ticker, change)
    retrieved_change = current_data_table.get_change(test_ticker)
    assert retrieved_change == change


def test_change_percent():
    change_percent = random_utilities.random_double()
    assert current_data_table.update_change_percent(test_ticker, change_percent)
    retrieved_change_percent = current_data_table.get_change_percent(test_ticker)
    assert retrieved_change_percent == change_percent


def test_beta():
    beta = random_utilities.random_double()
    assert current_data_table.update_beta(test_ticker, beta)
    retrieved_beta = current_data_table.get_beta(test_ticker)
    assert retrieved_beta == beta


def test_range():
    price_range = random_utilities.random_letters()
    assert current_data_table.update_range(test_ticker, price_range)
    retrieved_price_range = current_data_table.get_range(test_ticker)
    assert retrieved_price_range == price_range


def test_volume():
    volume = random_utilities.random_double()
    assert current_data_table.update_volume(test_ticker, volume)
    retrieved_volume = current_data_table.get_volume(test_ticker)
    assert retrieved_volume == volume


def test_market_cap():
    market_cap = random_utilities.random_double()
    assert current_data_table.update_market_cap(test_ticker, market_cap)
    retrieved_market_cap = current_data_table.get_market_cap(test_ticker)
    assert retrieved_market_cap == market_cap


def test_last_dividend():
    last_dividend = random_utilities.random_double()
    assert current_data_table.update_last_dividend(test_ticker, last_dividend)
    retrieved_last_dividend = current_data_table.get_last_dividend(test_ticker)
    assert retrieved_last_dividend == last_dividend


def test_dividend_ttm():
    dividend_ttm = random_utilities.random_double()
    assert current_data_table.update_dividend_ttm(test_ticker, dividend_ttm)
    retrieved_dividend_ttm = current_data_table.get_dividend_ttm(test_ticker)
    assert retrieved_dividend_ttm == dividend_ttm


def test_dividend_yield():
    dividend_yield = random_utilities.random_double()
    assert current_data_table.update_dividend_yield(test_ticker, dividend_yield)
    retrieved_dividend_yield = current_data_table.get_dividend_yield(test_ticker)
    assert retrieved_dividend_yield == dividend_yield


def test_dividend_years():
    dividend_years = random_utilities.random_int()
    assert current_data_table.update_dividend_years(test_ticker, dividend_years)
    retrieved_dividend_years = current_data_table.get_dividend_years(test_ticker)
    assert retrieved_dividend_years == dividend_years


def test_dividend_years_increasing():
    dividend_years_increasing = random_utilities.random_int()
    assert current_data_table.update_dividend_years_increasing(test_ticker, dividend_years_increasing)
    retrieved_dividend_years_increasing = current_data_table.get_dividend_years_increasing(test_ticker)
    assert retrieved_dividend_years_increasing == dividend_years_increasing


def test_payout_ratio_ttm():
    payout_ratio_ttm = random_utilities.random_double()
    assert current_data_table.update_payout_ratio_ttm(test_ticker, payout_ratio_ttm)
    retrieved_payout_ratio_ttm = current_data_table.get_payout_ratio_ttm(test_ticker)
    assert retrieved_payout_ratio_ttm == payout_ratio_ttm


def test_eps_ttm():
    eps_ttm = random_utilities.random_double()
    assert current_data_table.update_eps_ttm(test_ticker, eps_ttm)
    retrieved_eps_ttm = current_data_table.get_eps_ttm(test_ticker)
    assert retrieved_eps_ttm == eps_ttm
