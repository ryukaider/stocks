from config import database_config
from databases.tables.table import Table


class TickersTable(Table):
    columns = {
        'ticker': 'varchar PRIMARY KEY'
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
        stock_dict = {'ticker': stock.ticker}
        return self.insert_row(stock_dict)

    def remove_stocks(self, stocks):
        for stock in stocks:
            if self.remove_stock(stock) is False:
                return False
        return True

    def remove_stock(self, stock):
        return self.remove_row('ticker', stock.ticker)

    def get_tickers(self):
        query = f'SELECT ticker FROM {self.table_name} ORDER BY ticker ASC'
        rows = self.run_query(query)
        tickers = []
        for row in rows:
            tickers.append(row['ticker'])
        return tickers
