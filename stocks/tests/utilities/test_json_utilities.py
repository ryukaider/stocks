import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(_root_path)

import pytest
from utilities import json_utilities


def test_read_json():
    filepath = os.path.join(_root_path, '..', 'samples', 'alpha_vantage.json')
    json = json_utilities.read_json_file(filepath)
    assert json is not None
    assert len(json) > 0
