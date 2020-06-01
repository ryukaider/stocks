import datetime
from config import database_config
from databases import postgres
from databases.tables.table import Table
from databases.tables.tickers_table import TickersTable


class ApiProgressTable(Table):

    columns = {
        'ticker': 'text PRIMARY KEY NOT NULL',
        'daily_history': 'date'
    }

    def __init__(self,
                 name='api_progress',
                 database_name=database_config.database):
        Table.__init__(self, name, database_name, self.columns)

    def reset_all(self):
        ticker_list = TickersTable().get_tickers()
        for ticker in ticker_list:
            if not self.add_stock(ticker):
                self.reset_daily_history_progress(ticker)

    def add_stock(self, ticker):
        row = {'ticker': ticker}
        return self.insert_row(row)

    def update_daily_history_progress(self, ticker, date=datetime.datetime.now().date()):
        return self._update_progress(ticker, 'daily_history', date)

    def reset_daily_history_progress(self, ticker):
        query = f"UPDATE {self.name} SET daily_history = NULL WHERE ticker = '{ticker}'"
        return self.run_query(query)

    def get_daily_history_progress(self, days_old=1):
        date = (datetime.datetime.now() - datetime.timedelta(days=days_old)).date()
        query = f"SELECT ticker " \
                f"FROM {self.name} " \
                f"WHERE daily_history <= '{date}' " \
                f"OR daily_history IS NULL " \
                f"ORDER BY daily_history DESC"
        results = self.run_query(query)
        ticker_list = self._convert_results_to_tickers_list(results)
        return ticker_list

    def _update_progress(self, ticker, column, value):
        return postgres.update_value(self.cursor, self.name, 'ticker', ticker, column, value)

    @staticmethod
    def _convert_results_to_tickers_list(results):
        tickers_list = []
        for row in results:
            tickers_list.append(row['ticker'])
        return tickers_list
