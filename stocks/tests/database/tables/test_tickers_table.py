import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(_root_path)

import pytest
from database.tables import tickers_table


def test_exists():
    assert tickers_table.exists() is True


def test_create():
    assert tickers_table.create() is True


def test_get_tickers():
    assert tickers_table.get_tickers() is not None
