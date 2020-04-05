from database import postgres
from database import stocks_database

table_name = 'tickers'
columns = {'ticker': 'varchar PRIMARY KEY', 'exchange': 'varchar', 'name': 'varchar'}

cursor = stocks_database.get_cursor()


def exists():
    return postgres.table_exists(cursor, table_name)


def create():
    if not exists():
        return postgres.create_table(cursor, table_name, columns)
    return exists()

def add_stocks(stocks):
    for stock in stocks:
        if add_stock(stock) is False:
            return False
    return True


def add_stock(stock):
    stock_dict = {'ticker': stock.ticker, 'exchange': stock.exchange, 'name': stock.name}
    return postgres.insert_row_dict(cursor, table_name, stock_dict)


def remove_stocks(stocks):
    for stock in stocks:
        if remove_stock(stock) is False:
            return False
    return True
    

def remove_stock(stock):
    return postgres.remove_row(cursor, table_name, 'ticker', stock.ticker)


def get_tickers():
    query = f'SELECT ticker FROM {table_name} ORDER BY ticker ASC'
    postgres.run_query(cursor, query)
    return postgres.get_list_results(cursor)


create()


if __name__ == "__main__":
    get_tickers()
