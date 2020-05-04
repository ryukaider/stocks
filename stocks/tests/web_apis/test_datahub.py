from web_apis import datahub


def test_get_nyse_stocks():
    stocks = datahub.get_nyse_stocks_ticker_name_exchange()
    assert_stocks(stocks)


def test_get_nasdaq_stocks():
    stocks = datahub.get_nasdaq_stocks_ticker_name_exchange()
    assert_stocks(stocks)


def test_get_all_stocks():
    stocks = datahub.get_all_stocks_ticker_name_exchange()
    assert_stocks(stocks)


def assert_stocks(stocks):
    assert len(stocks) > 0
    for stock in stocks:
        assert stock.ticker is not None
        assert stock.exchange is not None
        assert stock.name is not None
