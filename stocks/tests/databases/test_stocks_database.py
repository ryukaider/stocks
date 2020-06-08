from databases.stocks_database import StocksDatabase

test_db = StocksDatabase('test')


def test_exists():
    assert test_db is not None


def test_name():
    assert test_db.name == 'test'


def test_tickers_table():
    assert test_db.tickers_table is not None


def test_api_progress_table():
    assert test_db.api_progress_table is not None
