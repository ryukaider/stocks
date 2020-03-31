import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(_root_path)

import psycopg2.extras
from database import postgres
from config import database_config
from config import keys_config


def get_cursor():
    database = database_config.database
    connection = postgres.connect(
        database_config.username,
        keys_config.database_password,
        database_config.host,
        database_config.port)
    cursor = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)
    if not postgres.database_exists(cursor, database):
        postgres.create_database(cursor, database)
    return connection
