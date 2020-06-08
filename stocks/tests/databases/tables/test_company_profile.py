import pytest
from config import database_config
from databases.database import Database
from databases.tables.company_profile_table import CompanyProfileTable
from utilities import random_utilities

database_name = database_config.test_database
table_name = 'test_company_profile'
test_ticker = 'TEST'
db = Database(database_name)
cursor = db.cursor()
company_profile_table = CompanyProfileTable(cursor, table_name)


@pytest.fixture(autouse=True, scope="class")
def setup_once_per_class():
    company_profile_table.add_stock(test_ticker)


def test_exists():
    assert company_profile_table.exists()


def test_create():
    assert company_profile_table.create()


def test_add_stock():
    ticker = random_utilities.random_letters(12)
    assert company_profile_table.add_stock(ticker)


def test_name():
    name = random_utilities.random_letters(12)
    assert company_profile_table.update_name(test_ticker, name)
    retrieved_name = company_profile_table.get_name(test_ticker)
    assert retrieved_name == name


def test_exchange():
    exchange = random_utilities.random_letters(8).upper()
    assert company_profile_table.update_exchange(test_ticker, exchange)
    retrieved_exchange = company_profile_table.get_exchange(test_ticker)
    assert retrieved_exchange == exchange


def test_exchange_new_york_stock_exchange():
    exchange = 'New York Stock Exchange'
    assert company_profile_table.update_exchange(test_ticker, exchange)
    retrieved_exchange = company_profile_table.get_exchange(test_ticker)
    assert retrieved_exchange == 'NYSE'


def test_exchange_usotc():
    exchange = 'US OTC'
    assert company_profile_table.update_exchange(test_ticker, exchange)
    retrieved_exchange = company_profile_table.get_exchange(test_ticker)
    assert retrieved_exchange == exchange


def test_exchange_none():
    exchange = None
    assert company_profile_table.update_exchange(test_ticker, exchange) is False


def test_sector():
    sector = random_utilities.random_letters(8)
    assert company_profile_table.update_sector(test_ticker, sector)
    retrieved_sector = company_profile_table.get_sector(test_ticker)
    assert retrieved_sector == sector


def test_sector_nonenergyminerals():
    sector = 'Energy Minerals'
    assert company_profile_table.update_sector(test_ticker, sector)
    retrieved_sector = company_profile_table.get_sector(test_ticker)
    assert retrieved_sector == 'Energy'


def test_industry():
    industry = random_utilities.random_letters(8)
    assert company_profile_table.update_industry(test_ticker, industry)
    retrieved_industry = company_profile_table.get_industry(test_ticker)
    assert retrieved_industry == industry


def test_description():
    description = random_utilities.random_letters(8)
    assert company_profile_table.update_description(test_ticker, description)
    retrieved_description = company_profile_table.get_description(test_ticker)
    assert retrieved_description == description


def test_ceo():
    ceo = random_utilities.random_letters(8)
    assert company_profile_table.update_ceo(test_ticker, ceo)
    retrieved_ceo = company_profile_table.get_ceo(test_ticker)
    assert retrieved_ceo == ceo


def test_employees():
    employees = random_utilities.random_int(1, 100000)
    assert company_profile_table.update_employees(test_ticker, employees)
    retrieved_employees = company_profile_table.get_employees(test_ticker)
    assert retrieved_employees == employees


def test_website():
    website = random_utilities.random_letters(8)
    assert company_profile_table.update_website(test_ticker, website)
    retrieved_website = company_profile_table.get_website(test_ticker)
    assert retrieved_website == website


def test_country():
    country = random_utilities.random_letters(2).upper()
    assert company_profile_table.update_country(test_ticker, country)
    retrieved_country = company_profile_table.get_country(test_ticker)
    assert retrieved_country == country


def test_ticker_not_found():
    ticker = random_utilities.random_string()
    with pytest.raises(Exception):
        company_profile_table.get_name(ticker)
