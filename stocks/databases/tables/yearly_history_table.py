from config import database_config
from databases import postgres
from databases.tables.table import Table


class YearlyHistoryTable(Table):
    columns = {
        'ticker': 'text NOT NULL',
        'year': 'numeric NOT NULL',
        'end_price': 'numeric (10, 2)',
        'average_price': 'numeric (10, 2)',
        'dividend': 'numeric (10, 2)',
        'average_dividend_yield': 'numeric (10, 2)',
        'UNIQUE': '(ticker, year)'
    }

    def __init__(self,
                 table_name='yearly_history',
                 database_name=database_config.database):
        Table.__init__(self, table_name, database_name, self.columns)

    def update_end_price(self, ticker, year, price):
        self.update_value(ticker, year, 'end_price', price)

    def update_average_price(self, ticker, year, price):
        self.update_value(ticker, year, 'average_price', price)

    def update_dividend(self, ticker, year, dividend):
        self.update_value(ticker, year, 'dividend', dividend)

    def update_dividend_yield(self, ticker, year, dividend_yield):
        self.update_value(ticker, year, 'dividend_yield', dividend_yield)

    def get_average_price(self, ticker, year):
        return self.get_value(ticker, year, 'average_price')

    def get_dividend(self, ticker, year):
        return self.get_value(ticker, year, 'dividend')

    def get_value(self, ticker, year, column):
        row = self.get_row(ticker, year)
        try:
            return float(row[column])
        except Exception:
            return None

    def get_data(self, ticker):
        query = f"SELECT * FROM {self.table_name} WHERE ticker = '{ticker}' ORDER BY year DESC"
        postgres.run_query(self.cursor, query)
        data = self.cursor.fetchall()
        return data

    def update_value(self, ticker, year, column, value):
        self.add_row(ticker, year)
        update_query = \
            f"UPDATE {self.table_name} " \
            f"SET {column} = {value} " \
            f"WHERE ticker = '{ticker}' " \
            f"AND year = {year}"
        return postgres.run_query(self.cursor, update_query)

    def add_row(self, ticker, year):
        if self.row_exists(ticker, year):
            return
        row = {
            'ticker': ticker,
            'year': year
        }
        postgres.insert_row_as_dict(self.cursor, self.table_name, row)

    def row_exists(self, ticker, year):
        row = len(self.get_row(ticker, year))
        return row is not None

    def get_row(self, ticker, year):
        query = f"SELECT * FROM {self.table_name} WHERE ticker = '{ticker}' AND year = {year}"
        postgres.run_query(self.cursor, query)
        rows = self.cursor.fetchall()
        row_count = len(rows)
        if row_count > 1:
            raise Exception(f'{self.table_name} contains more than one row for {ticker} - {year}')
        if row_count == 0:
            return None
        return rows[0]
