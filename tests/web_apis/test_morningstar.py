import pytest
from web_apis import morningstar


@pytest.mark.skip()
def test_get_financial_data():
    morningstar.get_financial_data()


@pytest.mark.skip()
def test_get_query():
    morningstar._get_query()


@pytest.mark.skip()
def test_convert_exchange():
    morningstar._convert_exchange()
