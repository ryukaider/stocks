import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(_root_path)

import pytest
from database.tables.table import Table

table_name = 'test'


def test_table():
    table = Table(table_name)
    assert table is not None


def test_exists():
    table = Table(table_name)
    assert table.exists()


def test_create():
    table = Table(table_name)
    assert table.create()
