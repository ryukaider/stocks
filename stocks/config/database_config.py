import os
from utilities import json_utilities

_root_path = os.path.join(os.path.dirname(__file__), '..')
_config_path = os.path.join(_root_path, 'config')
_database_config_path = os.path.join(_config_path, 'database_config.json')

username = json_utilities.read_json_file(_database_config_path)['server']['username']
host = json_utilities.read_json_file(_database_config_path)['server']['host']
port = json_utilities.read_json_file(_database_config_path)['server']['port']
database = json_utilities.read_json_file(_database_config_path)['primary database']
test_database = json_utilities.read_json_file(_database_config_path)['test database']
