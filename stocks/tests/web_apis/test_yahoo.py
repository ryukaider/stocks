import os, sys
root_path = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(root_path)

import pytest
from web_apis import yahoo


@pytest.mark.skip()
def test_get_summary_data():
    yahoo.get_summary_data()


@pytest.mark.skip()
def test_get_eps_ttm():
    yahoo.get_eps_ttm()


@pytest.mark.skip()
def test_get_eps_ttm_from_response():
    yahoo._get_eps_ttm_from_response()


@pytest.mark.skip()
def test_is_number():
    yahoo._is_number()
