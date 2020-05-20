from config import database_config
from databases import postgres
from databases.tables.table import Table


class TickersTable(Table):
    columns = {
        'ticker': 'varchar PRIMARY KEY',
        'exchange': 'varchar',
        'name': 'varchar'
    }

    def __init__(self,
                 table_name='tickers',
                 database_name=database_config.database):
        Table.__init__(self, table_name, database_name, self.columns)

    def add_stocks(self, stocks):
        for stock in stocks:
            if self.add_stock(stock) is False:
                return False
        return True

    def add_stock(self, stock):
        stock_dict = {'ticker': stock.ticker, 'exchange': stock.exchange, 'name': stock.name}
        return postgres.insert_row_as_dict(self.cursor, self.table_name, stock_dict)

    def remove_stocks(self, stocks):
        for stock in stocks:
            if self.remove_stock(stock) is False:
                return False
        return True

    def remove_stock(self, stock):
        return postgres.remove_row(self.cursor, self.table_name, 'ticker', stock.ticker)

    def get_tickers(self):
        query = f'SELECT ticker FROM {self.table_name} ORDER BY ticker ASC'
        postgres.run_query(self.cursor, query)
        return postgres.get_list_results(self.cursor)
