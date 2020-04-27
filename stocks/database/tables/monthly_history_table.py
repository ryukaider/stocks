from database import postgres
from database.tables.table import Table

class MonthlyHistoryTable(Table):

    columns = {
        'ticker': 'text NOT NULL',
        'date': 'date NOT NULL',
        'price': 'double precision',
        'dividend': 'double precision',
        'UNIQUE': '(ticker, date)'
    }


    def __init__(self, table_name='monthly_history'):
        Table.__init__(self, table_name)


    def add_monthly_data(self, monthly_data):
        for row in monthly_data:
            add_monthly_row(row)


    def add_monthly_row(self, monthly_row):
        if not postgres.insert_row(self.cursor, self.table_name, '(ticker, date, price, dividend)',
            f"('{monthly_row['ticker']}','{monthly_row['date']}','{monthly_row['price']}','{monthly_row['dividend']}')"):
            update_query = f"UPDATE {self.table_name} SET price = '{monthly_row['price']}' WHERE ticker = '{monthly_row['ticker']}' AND date = '{monthly_row['date']}'"
            postgres.run_query(self.cursor, update_query)


    def get_history(self, ticker):
        query = f"SELECT * FROM {self.table_name} WHERE ticker = '{ticker}' ORDER BY date DESC"
        postgres.run_query(self.cursor, query)
        data = self.cursor.fetchall()
        return data


    def get_date_dividend(self, ticker):
        query = f"SELECT date,dividend FROM {self.table_name} WHERE ticker = '{ticker}' ORDER BY date DESC"
        postgres.run_query(self.cursor, query)
        data = self.cursor.fetchall()
        return data


    def get_dividend_ttm(self, ticker):
        query = f"SELECT dividend FROM {self.table_name} WHERE ticker = '{ticker}' ORDER BY date DESC LIMIT 12"
        postgres.run_query(self.cursor, query)
        dividends = postgres.get_list_results(self.cursor)
        return dividends


    def get_latest_price(self, ticker):
        query = f"SELECT price FROM {self.table_name} WHERE ticker = '{ticker}' ORDER BY date DESC LIMIT 1"
        postgres.run_query(self.cursor, query)
        try:
            price = postgres.get_list_results(self.cursor)[0]
            return price
        except:
            return None
