import json
import pytest
from web_apis import alpha_vantage


def test_get_query():
    query = alpha_vantage._get_query('test', 'MSFT')
    assert 'test' in query
    assert 'MSFT' in query
    assert alpha_vantage.base_url in query
    assert alpha_vantage.api_key in query


@pytest.mark.skip('Uses API quota')
def test_get_monthly_data():
    alpha_vantage.get_monthly_history('MSFT')


def read_json_file():
    with open("stock_data/web_apis/example.json", "r") as json_file:
        data = json.load(json_file)
    return data
