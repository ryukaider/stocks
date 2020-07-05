from config import database_config
from database.stocks_database import StocksDatabase
from database_updaters.company_profile.company_profile_updater import CompanyProfileUpdater
from utilities import random_utilities

db = StocksDatabase(database_config.test_database)
company_profile_updater = CompanyProfileUpdater(db)


def test_update():
    assert company_profile_updater.update('MSFT') is True


def test_update_invalid_ticker():
    ticker = random_utilities.random_letters()
    assert company_profile_updater.update(ticker) is False
