import os, sys
root_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root_path)
import psycopg2.extras
from database import postgres
from utilities import json_utilities

database_config_path = os.path.join(sys.path[0], '..', '..', '..', 'config', 'database.json')
keys_config_path = os.path.join(sys.path[0], '..', '..', '..', 'config', 'keys.json')

username = json_utilities.read_json_file(database_config_path)['server']['username']
password = json_utilities.read_json_file(keys_config_path)['database_password']
host = json_utilities.read_json_file(database_config_path)['server']['host']
port = json_utilities.read_json_file(database_config_path)['server']['port']
database = json_utilities.read_json_file(database_config_path)['primary database']

connection = postgres.connect(username, password, host, port, database)
cursor = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)

if __name__ == "__main__":
    pass
