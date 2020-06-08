import datetime
from databases import postgres
from databases.tables.table import Table
from databases.tables.tickers_table import TickersTable


class ApiProgressTable(Table):

    columns = {
        'ticker': 'text PRIMARY KEY NOT NULL',
        'company_profile': 'date',
        'daily_history': 'date'
    }

    def __init__(self, cursor, name='api_progress'):
        Table.__init__(self, cursor, name, self.columns)

    def reset_all(self):
        ticker_list = TickersTable().get_tickers()
        for ticker in ticker_list:
            if not self.add_ticker(ticker):
                self.reset_daily_history_progress(ticker)

    def add_tickers(self, tickers):
        for ticker in tickers:
            self.add_ticker(ticker)

    def add_ticker(self, ticker):
        row = {'ticker': ticker}
        return self.insert_row(row)

    def update_daily_history_progress(self, ticker, date=datetime.datetime.now().date()):
        return self._update_progress(ticker, 'daily_history', date)

    def reset_daily_history_progress(self, ticker):
        return self._reset_progress(ticker, 'daily_history')

    def get_daily_history_progress(self, days_old=7):
        return self._get_progress('daily_history', days_old)

    def update_company_profile_progress(self, ticker, date=datetime.datetime.now().date()):
        return self._update_progress(ticker, 'company_profile', date)

    def reset_company_profile_progress(self, ticker):
        return self._reset_progress(ticker, 'company_profile')

    def get_company_profile_progress(self, days_old=30):
        return self._get_progress('company_profile', days_old)

    def _update_progress(self, ticker, column, value):
        return postgres.update_value(self.cursor, self.name, 'ticker', ticker, column, value)

    def _reset_progress(self, ticker, column):
        query = f"UPDATE {self.name} SET {column} = NULL WHERE ticker = '{ticker}'"
        return self.run_query(query)

    def _get_progress(self, column, days_old=1):
        date = (datetime.datetime.now() - datetime.timedelta(days=days_old)).date()
        query = f"SELECT ticker " \
                f"FROM {self.name} " \
                f"WHERE {column} <= '{date}' " \
                f"OR {column} IS NULL " \
                f"ORDER BY daily_history ASC NULLS FIRST"
        results = self.run_query(query)
        ticker_list = self._convert_results_to_tickers_list(results)
        return ticker_list

    @staticmethod
    def _convert_results_to_tickers_list(results):
        tickers_list = []
        for row in results:
            tickers_list.append(row['ticker'])
        return tickers_list
