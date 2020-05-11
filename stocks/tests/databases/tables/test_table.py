from config import database_config
from databases.tables.table import Table

database_name = database_config.test_database
table_name = 'test'
table = Table(table_name, database_name)


def test_table():
    assert table is not None


def test_exists():
    assert table.exists()


def test_create():
    assert table.create()
