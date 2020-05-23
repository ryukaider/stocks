import pytest
from api_to_database_table import alpha_vantage_to_monthly_history


@pytest.mark.skip()
def test_update():
    alpha_vantage_to_monthly_history.update_all()


@pytest.mark.skip()
def test_add_monthly_data_to_database():
    alpha_vantage_to_monthly_history.add_monthly_data_to_database()
