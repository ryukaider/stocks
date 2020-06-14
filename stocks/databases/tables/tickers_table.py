from .table import Table


class TickersTable(Table):
    columns = {
        'ticker': 'varchar PRIMARY KEY'
    }

    def __init__(self, cursor, name='tickers'):
        Table.__init__(self, cursor, name, self.columns)

    def add_tickers(self, tickers):
        values = ''
        for ticker in tickers:
            values += f"('{ticker}'),"
        values = values.strip(',')
        query = f'INSERT INTO {self.name} (ticker) VALUES {values} ON CONFLICT DO NOTHING;'
        return self.run_query(query)

    def add_ticker(self, ticker):
        row = {'ticker': ticker}
        return self.insert_row(row)

    def remove_tickers(self, tickers):
        for ticker in tickers:
            if self.remove_ticker(ticker) is False:
                return False
        return True

    def remove_ticker(self, ticker):
        return self.delete_row('ticker', ticker)

    def get_tickers(self):
        query = f'SELECT ticker FROM {self.name} ORDER BY ticker ASC'
        rows = self.run_query(query)
        tickers = []
        for row in rows:
            tickers.append(row['ticker'])
        return tickers
