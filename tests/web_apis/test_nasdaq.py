import pytest
from web_apis import nasdaq


@pytest.mark.skip
def test_get_nasdaq_tickers():
    tickers = nasdaq.get_nasdaq_tickers()
    assert len(tickers) > 0


@pytest.mark.skip
def test_get_nyse_tickers():
    tickers = nasdaq.get_nyse_tickers()
    assert len(tickers) > 0


def test_get_all_tickers():
    tickers = nasdaq.get_all_tickers()
    assert len(tickers) > 3000
    assert len(tickers) < 20000
    for ticker in tickers:
        assert isinstance(ticker, str) is True
        assert len(ticker) > 0
        assert len(ticker) < 7
        assert ticker.__contains__('|') is False
        assert ticker is not 'Symbol'
