import os, sys
root_path = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(root_path)

import pytest
from database import postgres
from utilities import random_utilities
from config import database_config
from config import keys_config


@pytest.fixture(autouse=True, scope="class")
def setup_once_per_class():
    print('Setup: Once per class')
    connection = _get_connection_to_server()
    cursor = connection.cursor()
    database = database_config.database
    postgres.create_database(cursor, database)


@pytest.fixture
def connection():
    connection = _get_connection_to_database()
    yield connection
    postgres.close_connection(connection)


@pytest.fixture
def cursor():
    connection = _get_connection_to_database()
    cursor = connection.cursor()
    yield cursor
    postgres.close_connection(connection, cursor)


@pytest.fixture
def table_name(cursor):
    table_name = 'test'
    columns = {'id': 'varchar(10) PRIMARY KEY'}
    postgres.create_table(cursor, table_name, columns)
    return table_name


def _get_connection_to_server():
    return postgres.connect(
        username=database_config.username,
        password=keys_config.database_password,
        host=database_config.host,
        port=database_config.port
    )


def _get_connection_to_database():
    return postgres.connect(
        username=database_config.username,
        password=keys_config.database_password,
        host=database_config.host,
        port=database_config.port,
        database=database_config.database
    )


def test_connect_no_database():
    connection = _get_connection_to_server()
    assert connection is not None


def test_connect_valid():
    connection = _get_connection_to_database()
    assert connection is not None


def test_connect_no_inputs():
    bad_connection = postgres.connect(None, None, None, None, None)
    assert bad_connection is None


def test_close_connection_valid_connection_and_cursor(connection, cursor):
    assert postgres.close_connection(connection, cursor)


def test_close_connection_valid_connection(connection):
    assert postgres.close_connection(connection)


def test_close_connection_invalid_connection():
    connection_closed = postgres.close_connection(None, None)
    assert connection_closed is False


def test_get_version(cursor):
    version = postgres.get_version(cursor)
    assert version is not None


def test_database_exists(cursor):
    assert postgres.database_exists(cursor, 'postgres') is True


def test_database_doesnt_exist(cursor):
    database_name = random_utilities.random_letters()
    assert postgres.database_exists(cursor, database_name) is False


@pytest.mark.skip('slow test')
def test_create_database():
    connection = _get_connection_to_server()
    cursor = connection.cursor()
    name = random_utilities.random_letters()
    assert postgres.create_database(cursor, name) is True
    postgres.delete_database(cursor, name)


def test_create_database_invalid_name():
    connection = _get_connection_to_server()
    cursor = connection.cursor()
    name = '0test'
    assert postgres.create_database(cursor, name) is False
    postgres.delete_database(cursor, name)


@pytest.mark.skip('tested in create database case')
def delete_database():
    pass


def test_create_table_no_columns(cursor):
    with pytest.raises(Exception):
        postgres.create_table(cursor, 'test', None)


def test_create_table_one_column(cursor):
    table_name = random_utilities.random_letters()
    columns = {'id': 'varchar(10) PRIMARY KEY'}
    assert postgres.create_table(cursor, table_name, columns) is True
    postgres.delete_table(cursor, table_name)


@pytest.mark.skip('tested in create table case')
def delete_database():
    pass


def test_add_column(cursor, table_name):
    column_name = random_utilities.random_letters()
    assert postgres.add_column(cursor, table_name, column_name) is True
    postgres.delete_column(cursor, table_name, column_name)


def test_add_column_invalid(cursor, table_name):
    assert postgres.add_column(cursor, table_name, None, None) == False


def test_delete_column(cursor, table_name):
    column_name = random_utilities.random_letters()
    postgres.add_column(cursor, table_name, column_name)
    assert postgres.delete_column(cursor, table_name, column_name) is True


def test_delete_column_invalid(cursor, table_name):
    assert postgres.delete_column(cursor, table_name, None) is False


def test_insert_row(cursor, table_name):
    columns = '(id)'
    values = f"('{random_utilities.random_letters()}')"
    assert postgres.insert_row(cursor, table_name, columns, values) is True


def test_insert_row_invalid(cursor, table_name):
    columns = f'(invalid)'
    values = f"('{random_utilities.random_letters()}')"
    assert postgres.insert_row(cursor, table_name, columns, values) is False


def test_insert_row_dict(cursor, table_name):
    values = {
        'id': random_utilities.random_letters(10)
    }
    assert postgres.insert_row_dict(cursor, table_name, values) is True


def test_insert_row_dict_invalid(cursor, table_name):
    values = {
        'invalid': random_utilities.random_letters(10)
    }
    assert postgres.insert_row_dict(cursor, table_name, values) is False


def test_update_row(cursor, table_name):
    column = 'id'
    columns = f'({column})'
    value = random_utilities.random_letters()
    values = f"('{value}')"
    postgres.insert_row(cursor, table_name, columns, values)
    new_value = f"('{random_utilities.random_letters()}')"
    assert postgres.update_row(cursor, table_name, column, values, column, new_value) is True


def test_update_row_invalid(cursor, table_name):
    assert postgres.update_row(cursor, table_name, None, None, None, None) is False


def test_remove_row(cursor, table_name):
    column = 'id'
    columns = f'({column})'
    value = random_utilities.random_letters()
    values = f"('{value}')"
    postgres.insert_row(cursor, table_name, columns, values)
    assert postgres.remove_row(cursor, table_name, column, value) is True


def test_remove_row_invalid(cursor, table_name):
    assert postgres.remove_row(cursor, table_name, None, None) is False


def test_run_query(cursor, table_name):
    query = f'SELECT * FROM {table_name}'
    assert postgres.run_query(cursor, query) is True


def test_run_query_invalid(cursor):
    query = 'SELECT *'
    assert postgres.run_query(cursor, query) is False


def test_get_list_results(cursor, table_name):
    query = f'SELECT * from {table_name}'
    postgres.run_query(cursor, query)
    results = postgres.get_list_results(cursor)
    assert len(results) > 0


def test_get_list_results_invalid():
    with pytest.raises(Exception):
        postgres.get_list_results(None)
