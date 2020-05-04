import psycopg2.extras
from database import stocks_database


def database_name_exists():
    assert stocks_database.database is not None
    

def test_exists():
    assert stocks_database.exists() is True


def test_create():
    assert stocks_database.create() is True


def test_get_cursor_with_database():
    cursor = stocks_database.get_cursor(True)
    assert type(cursor) is psycopg2.extras.DictCursor


def test_get_cursor_without_database():
    cursor = stocks_database.get_cursor(False)
    assert type(cursor) is psycopg2.extras.DictCursor


def test_get_connection_with_database():
    connnection = stocks_database.get_connection(True)
    ctype = type(connnection)
    assert type(connnection) is psycopg2.extensions.connection


def test_get_connection_without_database():
    connnection = stocks_database.get_connection(False)
    ctype = type(connnection)
    assert type(connnection) is psycopg2.extensions.connection
