import os, sys
root_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root_path)

import pytest
from stock import Stock


def test_stock_exists():
    new_stock = Stock()
    assert new_stock is not None
