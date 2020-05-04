import os
from utilities import json_utilities

_root_path = os.path.join(os.path.dirname(__file__), '..')
_config_path = os.path.join(_root_path, 'config')
_keys_config_path = os.path.join(_config_path, 'keys_config.json')

database_password = json_utilities.read_json_file(_keys_config_path)['database_password']
alpha_vantage_api_key = json_utilities.read_json_file(_keys_config_path)['alpha_vantage_api_key']
