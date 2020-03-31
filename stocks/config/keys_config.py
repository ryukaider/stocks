import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(_root_path)

from utilities import json_utilities

_config_path = os.path.join(_root_path, 'config')
_keys_config_path = os.path.join(_config_path, 'keys_config.json')

database_password = json_utilities.read_json_file(_keys_config_path)['database_password']