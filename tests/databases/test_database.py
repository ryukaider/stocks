import psycopg2.extras
from database.database import Database
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
    cursor = database.cursor(True)
    assert type(cursor) is psycopg2.extras.DictCursor


def test_get_cursor_without_database():
    cursor = database.cursor(False)
    assert type(cursor) is psycopg2.extras.DictCursor
