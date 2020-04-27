from database import postgres
from database.tables.table import Table

class YearlyHistoryTable(Table):

    columns = {
        'ticker': 'text NOT NULL',
        'year': 'numeric NOT NULL',
        'end_price': 'double precision',
        'average_price': 'double precision',
        'dividend': 'double precision',
        'dividend_yield': 'double precision',
        'UNIQUE': '(ticker, year)'
    }


    def __init__(self, table_name='yearly_history'):
        Table.__init__(self, table_name)


    def update_end_price(self, ticker, year, price):
        if not postgres.insert_row(self.cursor, self.table_name, '(ticker,year,end_price)', f"('{ticker}',{year},{price})"):
            update_query = f"UPDATE {self.table_name} SET end_price = {price} WHERE ticker = '{ticker}' AND year = {year}"
            postgres.run_query(self.cursor, update_query)


    def update_average_price(self, ticker, year, price):
        if not postgres.insert_row(self.cursor, self.table_name, '(ticker,year,average_price)', f"('{ticker}',{year},{price})"):
            update_query = f"UPDATE {self.table_name} SET average_price = {price} WHERE ticker = '{ticker}' AND year = {year}"
            postgres.run_query(self.cursor, update_query)


    def update_dividend(self, ticker, year, dividend):
        if not postgres.insert_row(self.cursor, self.table_name, '(ticker,year,dividend)', f"('{ticker}',{year},{dividend})"):
            update_query = f"UPDATE {self.table_name} SET dividend = {dividend} WHERE ticker = '{ticker}' AND year = {year}"
            postgres.run_query(self.cursor, update_query)


    def update_dividend_yield(self, ticker, year, dividend_yield):
        if not postgres.insert_row(self.cursor, self.table_name, '(ticker,year,dividend_yield)', f"('{ticker}',{year},{dividend_yield})"):
            update_query = f"UPDATE {self.table_name} SET dividend_yield = {dividend_yield} WHERE ticker = '{ticker}' AND year = {year}"
            postgres.run_query(self.cursor, update_query)


    def get_data(self, ticker):
        query = f"SELECT * FROM {self.table_name} WHERE ticker = '{ticker}' ORDER BY year DESC"
        postgres.run_query(self.cursor, query)
        data = self.cursor.fetchall()
        return data
