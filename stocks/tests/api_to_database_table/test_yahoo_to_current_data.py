import pytest
from api_to_database_table import yahoo_to_current_data


@pytest.mark.skip()
def test_add_all_eps_ttm():
    yahoo_to_current_data.add_all_eps_ttm()


@pytest.mark.skip()
def test_add_eps_ttm():
    yahoo_to_current_data.add_eps_ttm()
