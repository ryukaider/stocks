import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..', '..')
sys.path.append(_root_path)

from database import postgres
from database import stocks_database

table_name = 'tickers'
columns = {'ticker': 'varchar'}

def create():
    cursor = stocks_database.get_cursor()
    return postgres.create_table(cursor, table_name, columns)


def get_tickers():
    query = 'SELECT ticker FROM current_data ORDER BY ticker ASC'
    postgres.run_query(stocks_database.cursor, query)
    return postgres.get_list_results(stocks_database.cursor)


if __name__ == "__main__":
    get_tickers()
