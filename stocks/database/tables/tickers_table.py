import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(_root_path)

from database import postgres
from database import stocks_database

table_name = 'tickers'
columns = {'ticker': 'varchar'}

cursor = stocks_database.get_cursor()


def exists():
    return postgres.table_exists(cursor, table_name)


def create():
    if not exists():
        return postgres.create_table(cursor, table_name, columns)
    return exists()


def get_tickers():
    query = f'SELECT ticker FROM {table_name} ORDER BY ticker ASC'
    postgres.run_query(cursor, query)
    return postgres.get_list_results(cursor)


create()


if __name__ == "__main__":
    get_tickers()
