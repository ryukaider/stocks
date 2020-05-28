from web_apis import nasdaq


def test_get_all_tickers():
    tickers = nasdaq.get_all_tickers()
    assert len(tickers) > 0
    for ticker in tickers:
        assert isinstance(ticker, str) is True
        assert ticker.__contains__('|') is False
        assert ticker is not 'Symbol'
