import os
import sys
sys.path.append(os.path.join(sys.path[0], '..', '..'))
from database import postgres
from database import stocks_database


def create():
    pass


def get_tickers():
    query = 'SELECT ticker FROM current_data ORDER BY ticker ASC'
    postgres.run_query(stocks_database.cursor, query)
    return postgres.get_list_results(stocks_database.cursor)


if __name__ == "__main__":
    get_tickers()
