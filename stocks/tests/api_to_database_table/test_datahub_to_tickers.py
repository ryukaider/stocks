import pytest
from api_to_database_table import datahub_to_tickers


@pytest.mark.skip()
def test_add_tickers():
    datahub_to_tickers.update_tickers()
