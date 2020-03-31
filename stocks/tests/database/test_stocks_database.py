import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(_root_path)

import pytest
import psycopg2.extras
from database import stocks_database


def test_get_cursor():
    cursor = stocks_database.get_cursor()
    assert type(cursor) is psycopg2.extras.DictCursor
