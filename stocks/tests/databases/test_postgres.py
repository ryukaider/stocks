import pytest
from config import database_config
from config import keys_config
from databases import postgres
from utilities import random_utilities


test_table_name = 'test_table'
test_table_row_id = 'test_id'


@pytest.fixture(autouse=True, scope="class")
def setup_once_per_class():
    print('Setup: Once per class')
    connection = _get_connection_to_server()
    cursor = connection.cursor()
    database = database_config.test_database
    postgres.create_database(cursor, database)
    connection = _get_connection_to_database()
    cursor = connection.cursor()
    _create_test_table(cursor)
    _insert_test_table_row(cursor)


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
        database=database_config.test_database
    )


def _create_test_table(cursor):
    columns = {
        'id': 'varchar(10) PRIMARY KEY',
        'numeric_col': 'numeric',
        'date_col': 'date'
    }
    postgres.create_table(cursor, test_table_name, columns)


def _insert_test_table_row(cursor):
    columns = '(id)'
    values = f"('{test_table_row_id}')"
    postgres.insert_row(cursor, test_table_name, columns, values)


def test_connect_no_database():
    connection = _get_connection_to_server()
    assert connection is not None


def test_connect_valid():
    connection = _get_connection_to_database()
    assert connection is not None


def test_connect_no_inputs():
    bad_connection = postgres.connect(None, None, None, None, None)
    assert bad_connection is None


def test_cursor():
    cursor = postgres.cursor(
        username=database_config.username,
        password=keys_config.database_password,
        host=database_config.host,
        port=database_config.port,
        database=database_config.test_database
    )
    assert cursor is not None


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


@pytest.mark.skip('tested in create databases case')
def delete_database():
    pass


def test_table_doesnt_exist(cursor):
    table_name = "doesntexist"
    assert postgres.table_exists(cursor, table_name) is False


def test_table_exists_none(cursor):
    table_name = None
    assert postgres.table_exists(cursor, table_name) is False


def test_table_exists(cursor):
    assert postgres.table_exists(cursor, test_table_name) is True


def test_create_table_no_columns(cursor):
    table_name = random_utilities.random_letters_lowercase()
    assert postgres.create_table(cursor, table_name, None)
    postgres.delete_table(cursor, table_name)


def test_create_table_one_column(cursor):
    table_name = random_utilities.random_letters()
    columns = {'id': 'varchar(10) PRIMARY KEY'}
    assert postgres.create_table(cursor, table_name, columns) is True
    postgres.delete_table(cursor, table_name)


@pytest.mark.skip('tested in create table case')
def delete_database():
    pass


def test_add_column(cursor):
    column_name = random_utilities.random_letters()
    assert postgres.add_column(cursor, test_table_name, column_name) is True
    postgres.delete_column(cursor, test_table_name, column_name)


def test_add_column_invalid(cursor):
    assert postgres.add_column(cursor, test_table_name, None, None) is False


def test_delete_column(cursor):
    column_name = random_utilities.random_letters()
    postgres.add_column(cursor, test_table_name, column_name)
    assert postgres.delete_column(cursor, test_table_name, column_name) is True


def test_delete_column_invalid(cursor):
    assert postgres.delete_column(cursor, test_table_name, None) is False


def test_insert_row(cursor):
    columns = '(id)'
    values = f"('{random_utilities.random_letters()}')"
    assert postgres.insert_row(cursor, test_table_name, columns, values) is True


def test_insert_row_invalid(cursor):
    columns = f'(invalid)'
    values = f"('{random_utilities.random_letters()}')"
    assert postgres.insert_row(cursor, test_table_name, columns, values) is False


def test_insert_row_dict(cursor):
    values = {'id': random_utilities.random_letters(10)}
    assert postgres.insert_row_as_dict(cursor, test_table_name, values) is True


def test_insert_row_dict_apostrophe(cursor):
    value = "test'apo"
    values = {'id': value}
    assert postgres.insert_row_as_dict(cursor, test_table_name, values) is True
    postgres.remove_row(cursor, test_table_name, 'id', value)


def test_insert_row_dict_numeric(cursor):
    value = 101
    values = {
        'id': random_utilities.random_string(),
        'numeric_col': value
    }
    assert postgres.insert_row_as_dict(cursor, test_table_name, values) is True
    postgres.remove_row(cursor, test_table_name, 'numeric_col', value)


def test_insert_row_dict_invalid(cursor):
    values = {'invalid': random_utilities.random_letters(10)}
    assert postgres.insert_row_as_dict(cursor, test_table_name, values) is False


def test_update_row_string(cursor):
    new_value = random_utilities.random_letters()
    assert postgres.update_value(cursor, test_table_name, 'id', test_table_row_id, 'id', new_value) is True


def test_update_row_numeric(cursor):
    new_value = random_utilities.random_double()
    assert postgres.update_value(cursor, test_table_name, 'id', test_table_row_id, 'numeric_col', new_value) is True


def test_update_row_date(cursor):
    new_date = random_utilities.random_date()
    assert postgres.update_value(cursor, test_table_name, 'id', test_table_row_id, 'date_col', new_date) is True


def test_update_row_invalid(cursor):
    assert postgres.update_value(cursor, test_table_name, None, None, None, None) is False


def test_remove_row(cursor):
    column = 'id'
    columns = f'({column})'
    value = random_utilities.random_letters()
    values = f"('{value}')"
    postgres.insert_row(cursor, test_table_name, columns, values)
    assert postgres.remove_row(cursor, test_table_name, column, value) is True


def test_remove_row_invalid(cursor):
    assert postgres.remove_row(cursor, test_table_name, None, None) is False


def test_run_query(cursor):
    query = f'SELECT * FROM {test_table_name}'
    assert postgres.run_query(cursor, query) is True


def test_run_query_invalid(cursor):
    query = 'SELECT *'
    assert postgres.run_query(cursor, query) is False


def test_get_list_results(cursor):
    query = f'SELECT * from {test_table_name}'
    postgres.run_query(cursor, query)
    results = postgres.get_list_results(cursor)
    assert len(results) > 0


def test_get_list_results_invalid():
    with pytest.raises(Exception):
        postgres.get_list_results(None)
