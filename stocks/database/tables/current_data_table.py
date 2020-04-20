from database import postgres
from database.tables.table import Table

class CurrentDataTable(Table):
    
    columns = {
        'ticker': 'text PRIMARY KEY NOT NULL',
        'name': 'text',
        'exchange': 'text',
        'price': 'numeric',
        'dividend_ttm': 'numeric(5,2)',
        'dividend_yield': 'numeric(5,2)',
        'dividend_years': 'numeric',
        'dividend_years_increasing': 'numeric',
        'payout_ratio_ttm': 'numeric',
        'eps_ttm': 'numeric'
    }


    def __init__(self, table_name='current_data'):
        Table.__init__(self, table_name)


    def add_stock(self, ticker):
        structured_ticker = f"('{ticker}')"
        return postgres.insert_row(self.cursor, self.table_name, '(ticker)', structured_ticker)


    def update_name(self, ticker, name):
        return self._update_row(ticker, 'name', f"'{name}'")


    def update_exchange(self, ticker, exchange):
        return self._update_row(ticker, 'exchange', f"'{exchange}'")


    def update_price(self, ticker, price):
        return self._update_row(ticker, 'price', price)


    def update_dividend_ttm(self, ticker, dividend_ttm):
        return self._update_row(ticker, 'dividend_ttm', dividend_ttm)


    def update_dividend_yield(self, ticker, dividend_yield):
        return self._update_row(ticker, 'dividend_yield', dividend_yield)


    def update_dividend_years(self, ticker, dividend_years):
        return self._update_row(ticker, 'dividend_years', dividend_years)


    def update_dividend_years_increasing(self, ticker, dividend_years_increasing):
        return self._update_row(ticker, 'dividend_years_increasing', dividend_years_increasing)


    def update_payout_ratio_ttm(self, ticker, payout_ratio_ttm):
        return self._update_row(ticker, 'payout_ratio_ttm', payout_ratio_ttm)


    def update_eps_ttm(self, ticker, eps):
        return self._update_row(ticker, 'eps_ttm', eps)


    def _update_row(self, ticker, column, value):
        if value == None:
            return False
        return postgres.update_row(
            self.cursor, self.table_name, 'ticker', f"'{ticker}'", column, value)


    def get_name(self, ticker):
        return self._get_value(ticker, 'name')


    def get_exchange(self, ticker):
        return self._get_value(ticker, 'exchange')


    def get_price(self, ticker):
        return float(self._get_value(ticker, 'price'))


    def get_dividend_ttm(self, ticker):
        return float(self._get_value(ticker, 'dividend_ttm'))


    def get_dividend_yield(self, ticker):
        return float(self._get_value(ticker, 'dividend_yield'))


    def get_dividend_years(self, ticker):
        return float(self._get_value(ticker, 'dividend_years'))


    def get_dividend_years_increasing(self, ticker):
        return float(self._get_value(ticker, 'dividend_years_increasing'))


    def get_payout_ratio_ttm(self, ticker):
        return float(self._get_value(ticker, 'payout_ratio_ttm'))


    def get_eps_ttm(self, ticker):
        return float(self._get_value(ticker, 'eps_ttm'))


    def _get_value(self, ticker, column):
        query = f"SELECT {column} FROM {self.table_name} WHERE ticker = '{ticker}'"
        postgres.run_query(self.cursor, query)
        value = postgres.get_list_results(self.cursor)[0]
        return value
