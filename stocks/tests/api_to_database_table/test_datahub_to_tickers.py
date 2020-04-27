import os, sys
root_path = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(root_path)

import pytest
from api_to_database_table import datahub_to_tickers


@pytest.mark.skip()
def test_add_tickers():
    datahub_to_tickers.add_tickers()
