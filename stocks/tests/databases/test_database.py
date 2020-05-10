import psycopg2.extras
from databases.database import Database
from config import database_config


database_name = database_config.test_database
database = Database(database_name)


def database_name_exists():
    assert database is not None


def test_exists():
    assert database.exists() is True


def test_create():
    assert database.create() is True


def test_get_cursor_with_database():
    cursor = database.get_cursor(True)
    assert type(cursor) is psycopg2.extras.DictCursor


def test_get_cursor_without_database():
    cursor = database.get_cursor(False)
    assert type(cursor) is psycopg2.extras.DictCursor


def test_get_connection_with_database():
    connnection = database.get_connection(True)
    assert type(connnection) is psycopg2.extensions.connection


def test_get_connection_without_database():
    connnection = database.get_connection(False)
    assert type(connnection) is psycopg2.extensions.connection
