from .table.table import Table


class DividendsTable(Table):
    columns = {
        'ticker': 'text PRIMARY KEY NOT NULL',
        'last_dividend': 'numeric(9,2)',
        'dividend_ttm': 'numeric(9,2)',
        'dividend_yield_ttm': 'numeric(9,2)',
        'dividend_years': 'integer',
        'dividend_years_stable': 'integer',
        'dividend_years_increasing': 'integer',
        'payout_ratio_ttm': 'numeric(9,2)'
    }

    def __init__(self, cursor, name='dividends'):
        Table.__init__(self, cursor, name, self.columns)

    def add_stock(self, ticker):
        row = {'ticker': ticker}
        return self.insert_row(row)

    def update_last_dividend(self, ticker, last_dividend):
        return self._update_row(ticker, 'last_dividend', last_dividend)

    def update_dividend_ttm(self, ticker, dividend_ttm):
        return self._update_row(ticker, 'dividend_ttm', dividend_ttm)

    def update_dividend_yield_ttm(self, ticker, dividend_yield_ttm):
        return self._update_row(ticker, 'dividend_yield_ttm', dividend_yield_ttm)

    def update_dividend_years(self, ticker, dividend_years):
        return self._update_row(ticker, 'dividend_years', dividend_years)

    def update_dividend_years_stable(self, ticker, dividend_years_stable):
        return self._update_row(ticker, 'dividend_years_stable', dividend_years_stable)

    def update_dividend_years_increasing(self, ticker, dividend_years_increasing):
        return self._update_row(ticker, 'dividend_years_increasing', dividend_years_increasing)

    def update_payout_ratio_ttm(self, ticker, payout_ratio_ttm):
        return self._update_row(ticker, 'payout_ratio_ttm', payout_ratio_ttm)

    def _update_row(self, ticker, column, value):
        if value is None:
            return False
        return self.update_value('ticker', ticker, column, value)

    def get_last_dividend(self, ticker):
        return self._get_float_value(ticker, 'last_dividend')

    def get_dividend_ttm(self, ticker):
        return self._get_float_value(ticker, 'dividend_ttm')

    def get_dividend_yield_ttm(self, ticker):
        return self._get_float_value(ticker, 'dividend_yield_ttm')

    def get_dividend_years(self, ticker):
        return self._get_float_value(ticker, 'dividend_years')

    def get_dividend_years_stable(self, ticker):
        return self._get_float_value(ticker, 'dividend_years_stable')

    def get_dividend_years_increasing(self, ticker):
        return self._get_float_value(ticker, 'dividend_years_increasing')

    def get_payout_ratio_ttm(self, ticker):
        return self._get_float_value(ticker, 'payout_ratio_ttm')

    def _get_float_value(self, ticker, column):
        try:
            return float(self._get_value(ticker, column))
        except TypeError:
            return None

    def _get_value(self, ticker, column):
        query = f"SELECT {column} FROM {self.name} WHERE ticker = '{ticker}'"
        value = self.run_query(query)[0][column]
        return value
