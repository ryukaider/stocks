import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(_root_path)

import pytest
from config import keys_config


def test_config_path():
    assert keys_config._config_path is not None


def test_keys_config_path():
    assert keys_config._keys_config_path is not None


def test_database_password():
    assert keys_config.database_password is not None


def test_alpha_vantage_api_key():
    assert keys_config.alpha_vantage_api_key is not None
