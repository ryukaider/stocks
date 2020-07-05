import datetime
from config import database_config
from database.database import Database
from database.tables.table_progress_table import TableProgressTable
from utilities import random_utilities

db = Database(database_config.test_database)
table_progress_table = TableProgressTable(db.cursor())


def test_exists():
    assert table_progress_table.exists() is True


def test_create():
    assert table_progress_table.create() is True


def test_add_row():
    table_name = random_utilities.random_letters()
    assert table_progress_table.add_row(table_name) is True
    assert table_progress_table.get_last_updated(table_name) is None


def test_update_progress():
    table_name = random_utilities.random_letters()
    table_progress_table.add_row(table_name)
    assert table_progress_table.update_progress(table_name) is True


def test_get_last_updated():
    table_name = random_utilities.random_letters()
    table_progress_table.add_row(table_name)
    table_progress_table.update_progress(table_name)
    last_updated = table_progress_table.get_last_updated(table_name)
    assert last_updated == datetime.datetime.now().date()
