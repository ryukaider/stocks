from .table.table import Table


class DailyHistoryTable(Table):
    columns = {
        'ticker': 'text NOT NULL',
        'date': 'date NOT NULL',
        'open': 'numeric (10, 4)',
        'high': 'numeric (10, 4)',
        'low': 'numeric (10, 4)',
        'close': 'numeric (10, 4)',
        'adjusted_close': 'numeric (10, 4)',
        'volume': 'integer',
        'dividend': 'numeric (10, 4)',
        'adjusted_dividend': 'numeric (10, 4)',
        'split_coefficient': 'numeric (10, 4)',
        'UNIQUE': '(ticker, date)'
    }

    def __init__(self, cursor, name='daily_history'):
        Table.__init__(self, cursor, name, self.columns)

    def upsert(self, rows: list):
        primary_keys = ['ticker', 'date']
        return self._upsert_rows(rows, primary_keys)

    def get_history(self, ticker, year=None, orderby='DATE DESC'):
        query = f"SELECT * FROM {self.name} WHERE ticker = '{ticker}'"
        if year is not None:
            query += f" AND date >= '{year}-01-01' AND date <= '{year}-12-31'"
        query += f' ORDER BY {orderby};'
        return self.run_query(query)
