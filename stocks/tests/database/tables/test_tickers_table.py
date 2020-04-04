import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(_root_path)

import pytest
from database.tables import tickers_table

def test_create():
    assert tickers_table.create() is True
