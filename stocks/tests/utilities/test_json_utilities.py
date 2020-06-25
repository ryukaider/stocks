import os
from utilities import json_utilities

_root_path = os.path.join(os.path.dirname(__file__), '..', '..')


def test_read_json():
    filepath = os.path.join(_root_path, '..', 'external_api_samples', 'alpha_vantage_monthly_history.json')
    json = json_utilities.read_json_file(filepath)
    assert json is not None
    assert len(json) > 0
