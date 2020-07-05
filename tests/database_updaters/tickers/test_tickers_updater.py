from database.stocks_database import StocksDatabase
from database_updaters.tickers.tickers_updater import TickersUpdater
from database.tables.tickers_table import TickersTable

db = StocksDatabase()  # Real database for read-only tests
tickers_updater = TickersUpdater(db)
tickers_table = TickersTable(db.cursor())


def test_is_updatable_0():
    assert tickers_updater._is_updatable(0) is True


# Assumes that the database has been updated in the last year
def test_is_updatable_365():
    assert tickers_updater._is_updatable(365) is False


# Doesn't actually call update_all_tickers()
# Instead, assumes the table has been updated already, and gets the results from the table
def test_update_all_tickers():
    tickers = tickers_table.get_tickers()
    assert tickers is not None
    assert len(tickers) > 1000
    assert len(tickers) < 20000
    assert 'KO' in tickers  # NYSE ticker
    assert 'NFLX' in tickers  # NASDAQ ticker
    assert 'BRK.A' in tickers  # Stock with multiple share types
    assert 'BRK.B' in tickers  # Stock with multiple share types
    assert 'ACI' in tickers  # Recently added ticker
    assert 'GNC' not in tickers # Delisted ticker
    assert 'NRZ-A' in tickers  # Preferred shares
