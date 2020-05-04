from stock import Stock


def test_stock_exists():
    new_stock = Stock()
    assert new_stock is not None
