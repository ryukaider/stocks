import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(_root_path)

import psycopg2.extras
from database import postgres
from config import database_config
from config import keys_config

database = database_config.database


def exists():
    cursor = get_cursor(with_database=False)
    return postgres.database_exists(cursor, database)


def create():
    cursor = get_cursor(with_database=False)
    if not exists():
        return postgres.create_database(cursor, database)
    return cursor is not None


def get_cursor(with_database=True):
    connection = get_connection(with_database)
    cursor = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)
    return cursor


def get_connection(with_database=True):
    database_name = database if with_database else None
    return postgres.connect(
        database_config.username,
        keys_config.database_password,
        database_config.host,
        database_config.port,
        database_name)


create()
