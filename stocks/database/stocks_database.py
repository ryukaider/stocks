import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(_root_path)

import psycopg2.extras
from database import postgres
from config import database_config
from config import keys_config

username = database_config.username
host = database_config.host
port = database_config.port
database = database_config.database
password = keys_config.database_password


def get_cursor():
    connection = postgres.connect(username, password, host, port)
    cursor = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)
    if not postgres.database_exists(cursor, database):
        postgres.create_database(cursor, database)
    return connection
