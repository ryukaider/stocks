from config import database_config
from databases import postgres
from databases.tables.table import Table


class MonthlyHistoryTable(Table):
    columns = {
        'ticker': 'text NOT NULL',
        'date': 'date NOT NULL',
        'price': 'double precision',
        'dividend': 'double precision',
        'UNIQUE': '(ticker, date)'
    }

    def __init__(self,
                 name='monthly_history',
                 database_name=database_config.database):
        Table.__init__(self, name, database_name, self.columns)

    def add_monthly_data(self, monthly_data):
        for row in monthly_data:
            self.add_monthly_row(row)

    def add_monthly_row(self, monthly_row):
        columns = '(ticker, date, price, dividend)'
        values = f"('{monthly_row['ticker']}'," \
                 f"'{monthly_row['date']}'," \
                 f"'{monthly_row['price']}'," \
                 f"'{monthly_row['dividend']}')"
        if not postgres.insert_row(self.cursor, self.name, columns, values):
            update_query = \
                f"UPDATE {self.name} " \
                f"SET price = '{monthly_row['price']}' " \
                f"WHERE ticker = '{monthly_row['ticker']}' " \
                f"AND date = '{monthly_row['date']}'"
            postgres.run_query(self.cursor, update_query)

    def get_history(self, ticker):
        query = f"SELECT * FROM {self.name} WHERE ticker = '{ticker}' ORDER BY date DESC"
        postgres.run_query(self.cursor, query)
        data = self.cursor.fetchall()
        return data

    def get_date_dividend(self, ticker):
        query = f"SELECT date,dividend FROM {self.name} WHERE ticker = '{ticker}' ORDER BY date DESC"
        postgres.run_query(self.cursor, query)
        data = self.cursor.fetchall()
        return data

    def get_dividend_ttm(self, ticker):
        query = f"SELECT dividend FROM {self.name} WHERE ticker = '{ticker}' ORDER BY date DESC LIMIT 12"
        postgres.run_query(self.cursor, query)
        dividends = postgres.get_list_results(self.cursor)
        return dividends

    def get_latest_price(self, ticker):
        query = f"SELECT price FROM {self.name} WHERE ticker = '{ticker}' ORDER BY date DESC LIMIT 1"
        postgres.run_query(self.cursor, query)
        try:
            price = postgres.get_list_results(self.cursor)[0]
            return price
        except Exception:
            return None
