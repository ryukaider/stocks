from config import database_config
from database.database import Database
from database.tables.table import Table
from utilities import random_utilities

database_name = database_config.test_database
table_name = 'test'
key_column = 'test_col'
text_column = 'test_col2'
numeric_column = 'test_col3'
columns = {
    key_column: 'text PRIMARY KEY NOT NULL',
    text_column: 'text',
    numeric_column: 'numeric'
}

db = Database(database_name)
cursor = db.cursor()
table = Table(cursor, table_name, columns)


def test_table():
    assert table is not None


def test_exists():
    assert table.exists() is True


def test_create():
    assert table.create() is True


def test_add_column():
    column_name = 'test_add_col'
    assert table.add_column(column_name) is True
    table.delete_column(column_name)


def test_insert_row():
    row = {key_column: random_utilities.random_string()}
    assert table.insert_row(row) is True


def test_upsert_rows():
    pass


def test_delete_row():
    value = random_utilities.random_string()
    row = {key_column: value}
    table.insert_row(row)
    assert table.delete_row(key_column, value) is True


def test_get_all_rows():
    _insert_random_row()
    rows = table.get_all_rows()
    assert len(rows) > 0


def test_delete_all_rows():
    _insert_random_row()
    assert table.delete_all_rows() is True
    rows = table.get_all_rows()
    assert len(rows) == 0


def test_get_value_string():
    key_val = random_utilities.random_string()
    text_val = random_utilities.random_string()
    row = {
        key_column: key_val,
        text_column: text_val
    }
    table.insert_row(row)
    assert table.get_value(key_column, key_val, text_column) == text_val


def test_get_float_value():
    key_val = random_utilities.random_string()
    numeric_val = random_utilities.random_double()
    row = {
        key_column: key_val,
        numeric_column: numeric_val
    }
    table.insert_row(row)
    assert table.get_float_value(key_column, key_val, numeric_column) == numeric_val


def test_update_value():
    key_val = random_utilities.random_string()
    numeric_val = random_utilities.random_double()
    row = {
        key_column: key_val,
        numeric_column: numeric_val
    }
    table.insert_row(row)
    new_val = random_utilities.random_double()
    assert table.update_value(key_column, key_val, numeric_column, new_val) is True
    assert table.get_float_value(key_column, key_val, numeric_column) == new_val


def test_run_query():
    query = f'SELECT * FROM {table.name}'
    results = table.run_query(query)
    assert len(results) >= 1


def test_run_query_single_result():
    pass


def _insert_random_row():
    row = {
        key_column: random_utilities.random_letters(),
        numeric_column: random_utilities.random_int()
    }
    table.insert_row(row)
