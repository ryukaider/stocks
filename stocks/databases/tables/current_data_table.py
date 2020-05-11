from config import database_config
from databases import postgres
from databases.tables.table import Table


class CurrentDataTable(Table):
    columns = {
        'ticker': 'text PRIMARY KEY NOT NULL',
        'name': 'text',
        'exchange': 'text',
        'sector': 'text',
        'industry': 'text',
        'ceo': 'text',
        'website': 'text',
        'description': 'text',
        'price': 'numeric(10,2)',
        'change': 'numeric',
        'change_percent': 'numeric',
        'beta': 'numeric',
        'range': 'text',
        'volume': 'numeric',
        'market_cap': 'numeric',
        'last_dividend': 'numeric(5,2)',
        'dividend_ttm': 'numeric(5,2)',
        'dividend_yield': 'numeric(5,2)',
        'dividend_years': 'numeric',
        'dividend_years_increasing': 'numeric',
        'payout_ratio_ttm': 'numeric',
        'eps_ttm': 'numeric'
    }

    def __init__(self,
                 table_name='current_data',
                 database_name=database_config.database):
        Table.__init__(self, table_name, database_name, self.columns)

    def add_stock(self, ticker):
        structured_ticker = f"('{ticker}')"
        return postgres.insert_row(self.cursor, self.table_name, '(ticker)', structured_ticker)

    def update_name(self, ticker, name):
        return self._update_row(ticker, 'name', f"'{name}'")

    def update_exchange(self, ticker, exchange):
        return self._update_row(ticker, 'exchange', f"'{exchange}'")

    def update_sector(self, ticker, sector):
        return self._update_row(ticker, 'sector', f"'{sector}'")

    def update_industry(self, ticker, industry):
        return self._update_row(ticker, 'industry', f"'{industry}'")

    def update_ceo(self, ticker, ceo):
        return self._update_row(ticker, 'ceo', f"'{ceo}'")

    def update_website(self, ticker, website):
        return self._update_row(ticker, 'website', f"'{website}'")

    def update_description(self, ticker, description):
        return self._update_row(ticker, 'description', f"'{description}'")

    def update_price(self, ticker, price):
        return self._update_row(ticker, 'price', price)

    def update_change(self, ticker, change):
        return self._update_row(ticker, 'change', change)

    def update_change_percent(self, ticker, change_percent):
        return self._update_row(ticker, 'change_percent', change_percent)

    def update_beta(self, ticker, beta):
        return self._update_row(ticker, 'beta', beta)

    def update_range(self, ticker, price_range):
        return self._update_row(ticker, 'range', f"'{price_range}'")

    def update_volume(self, ticker, volume):
        return self._update_row(ticker, 'volume', volume)

    def update_market_cap(self, ticker, market_cap):
        return self._update_row(ticker, 'market_cap', market_cap)

    def update_last_dividend(self, ticker, last_dividend):
        return self._update_row(ticker, 'last_dividend', last_dividend)

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
        if value is None:
            return False
        return postgres.update_row(
            self.cursor, self.table_name, 'ticker', f"'{ticker}'", column, value)

    def get_name(self, ticker):
        return self._get_value(ticker, 'name')

    def get_exchange(self, ticker):
        return self._get_value(ticker, 'exchange')

    def get_sector(self, ticker):
        return self._get_value(ticker, 'sector')

    def get_industry(self, ticker):
        return self._get_value(ticker, 'industry')

    def get_ceo(self, ticker):
        return self._get_value(ticker, 'ceo')

    def get_website(self, ticker):
        return self._get_value(ticker, 'website')

    def get_description(self, ticker):
        return self._get_value(ticker, 'description')

    def get_price(self, ticker):
        return self._get_float_value(ticker, 'price')

    def get_change(self, ticker):
        return self._get_float_value(ticker, 'change')

    def get_change_percent(self, ticker):
        return self._get_float_value(ticker, 'change_percent')

    def get_beta(self, ticker):
        return self._get_float_value(ticker, 'beta')

    def get_range(self, ticker):
        return self._get_value(ticker, 'range')

    def get_volume(self, ticker):
        return self._get_float_value(ticker, 'volume')

    def get_market_cap(self, ticker):
        return self._get_float_value(ticker, 'market_cap')

    def get_last_dividend(self, ticker):
        return self._get_float_value(ticker, 'last_dividend')

    def get_dividend_ttm(self, ticker):
        return self._get_float_value(ticker, 'dividend_ttm')

    def get_dividend_yield(self, ticker):
        return self._get_float_value(ticker, 'dividend_yield')

    def get_dividend_years(self, ticker):
        return self._get_float_value(ticker, 'dividend_years')

    def get_dividend_years_increasing(self, ticker):
        return self._get_float_value(ticker, 'dividend_years_increasing')

    def get_payout_ratio_ttm(self, ticker):
        return self._get_float_value(ticker, 'payout_ratio_ttm')

    def get_eps_ttm(self, ticker):
        return self._get_float_value(ticker, 'eps_ttm')

    def _get_float_value(self, ticker, column):
        try:
            return float(self._get_value(ticker, column))
        except TypeError:
            return None

    def _get_value(self, ticker, column):
        query = f"SELECT {column} FROM {self.table_name} WHERE ticker = '{ticker}'"
        postgres.run_query(self.cursor, query)
        value = postgres.get_list_results(self.cursor)[0]
        return value
