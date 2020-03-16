import os
import sys
sys.path.append(os.path.join(sys.path[0], '..', '..'))
import pytest
from database import postgres
from utilities import utilities
from utilities import json_utilities

test_database = 'test'
test_table = 'sandbox'
test_column = 'test'
test_column_type = 'text'

database_config_path = os.path.join(sys.path[0], '..', '..', '..', 'config', 'database.json')
keys_config_path = os.path.join(sys.path[0], '..', '..', '..', 'config', 'keys.json')


@pytest.fixture(autouse=True, scope="module")
def setup_teardown():
    connection = _get_connection()
    cursor = connection.cursor()
    postgres.add_column(cursor, test_table, 'a', 'text')
    postgres.add_column(cursor, test_table, 'b', 'numeric')
    yield
    postgres.close_connection(connection, cursor)


@pytest.fixture
def connection():
    connection = _get_connection()
    yield connection
    postgres.close_connection(connection)


@pytest.fixture
def cursor():
    connection = _get_connection()
    cursor = connection.cursor()
    yield cursor
    postgres.close_connection(connection, cursor)


def _get_connection():
    return postgres.connect(
        username=json_utilities.read_json_file(database_config_path)['server']['username'],
        password=json_utilities.read_json_file(keys_config_path)['database_password'],
        host=json_utilities.read_json_file(database_config_path)['server']['host'],
        port=json_utilities.read_json_file(database_config_path)['server']['port'],
        database=json_utilities.read_json_file(database_config_path)['test database'])


def test_connect_valid(connection):
    assert connection is not None


@pytest.mark.skip
def test_connect_no_inputs():
    bad_connection = postgres.connect(None, None, None, None, None)
    assert bad_connection is None


@pytest.mark.skip
def test_close_connection_valid_connection_and_cursor(connection, cursor):
    assert postgres.close_connection(connection, cursor)


@pytest.mark.skip
def test_close_connection_valid_connection(connection):
    assert postgres.close_connection(connection)


@pytest.mark.skip
def test_close_connection_invalid_connection():
    connection_closed = postgres.close_connection(None, None)
    assert connection_closed == False


@pytest.mark.skip
def test_create_database():
    with pytest.raises(NotImplementedError):
        postgres.create_database()


@pytest.mark.skip
def test_create_table():
    with pytest.raises(NotImplementedError):
        postgres.create_table()


@pytest.mark.skip
def test_add_column(cursor):
    column = utilities.random_string()
    assert postgres.add_column(cursor, test_table, column, test_column_type)
    postgres.delete_column(cursor, test_table, column)


@pytest.mark.skip
def test_add_column_invalid(cursor):
    assert postgres.add_column(cursor, test_table, None, None) == False


@pytest.mark.skip
def test_delete_column(cursor):
    column = utilities.random_string()
    postgres.add_column(cursor, test_table, column, test_column_type)
    assert postgres.delete_column(cursor, test_table, column)


@pytest.mark.skip
def test_delete_column_invalid(cursor):
    assert postgres.delete_column(cursor, test_table, None) == False


@pytest.mark.skip
def test_insert_row(cursor):
    columns = f'({test_column})'
    values = f"('{utilities.random_string}')"
    assert postgres.insert_row(cursor, test_table, columns, values)


@pytest.mark.skip
def test_insert_row_invalid(cursor):
    columns = f'(invalid)'
    values = f"('{utilities.random_string}')"
    assert postgres.insert_row(cursor, test_table, columns, values) == False


@pytest.mark.skip
def test_insert_row_dict(cursor):
    values = {
        'a': 'test',
        'b': 1
    }
    assert postgres.insert_row_dict(cursor, test_table, values)


"""
def test_update_row(cursor):
    column = utilities.random_string
    postgres.insert_row(cursor, test_table, )
    postgres.update_row(cursor, test_table, test_column, )
    pass
"""
