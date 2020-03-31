import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(_root_path)

from database import postgres
from database import stocks_database


def create():
    
    postgres.create_table()


def get_tickers():
    query = 'SELECT ticker FROM current_data ORDER BY ticker ASC'
    postgres.run_query(stocks_database.cursor, query)
    return postgres.get_list_results(stocks_database.cursor)


if __name__ == "__main__":
    get_tickers()
