from databases import postgres
from databases.tables.table import Table
from databases.tables.tickers_table import TickersTable


class ApiProgressTable(Table):
    columns = {
        'ticker': 'text PRIMARY KEY NOT NULL',
        'monthly': 'boolean',
        'eps': 'boolean'
    }

    def __init__(self, table_name='api_progress'):
        Table.__init__(self, table_name)

    def reset_all(self):
        ticker_list = TickersTable().get_tickers()
        for ticker in ticker_list:
            if not self.add_stock(ticker):
                self.reset_monthly_progress(ticker)
                self.reset_eps_progress(ticker)

    def add_stock(self, ticker):
        return postgres.insert_row(
            self.cursor,
            self.table_name,
            '(ticker, monthly, eps)',
            f"('{ticker}',false,false)")

    def reset_monthly_progress(self, ticker):
        return self._update_progress(ticker, 'monthly', False)

    def set_monthly_done(self, ticker):
        return self._update_progress(ticker, 'monthly', True)

    def reset_eps_progress(self, ticker):
        return self._update_progress(ticker, 'eps', False)

    def set_eps_done(self, ticker):
        return self._update_progress(ticker, 'eps', True)

    def _update_progress(self, ticker, column, value):
        return postgres.update_row(
            self.cursor, self.table_name, 'ticker', f"'{ticker}'", column, value)

    def get_incomplete_stocks(self, column):
        query = f"SELECT ticker FROM {self.table_name} WHERE {column} is not true ORDER BY ticker ASC"
        postgres.run_query(self.cursor, query)
        tickers = postgres.get_list_results(self.cursor)
        return tickers
