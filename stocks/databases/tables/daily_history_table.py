from databases import postgres
from .table import Table


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
        'split_coefficient': 'numeric (10, 4)',
        'UNIQUE': '(ticker, date)'
    }

    def __init__(self, cursor, name='daily_history'):
        Table.__init__(self, cursor, name, self.columns)

    def add_rows(self, rows):
        values = ''
        for row in rows:
            values += f"('{row['ticker']}', " \
                      f"'{row['date']}', " \
                      f"{row['open']}, " \
                      f"{row['high']}, " \
                      f"{row['low']}, " \
                      f"{row['close']}, " \
                      f"{row['adjusted_close']}, " \
                      f"{row['volume']}, " \
                      f"{row['dividend']}, " \
                      f"{row['split_coefficient']}),"
        values = values.strip(',')
        query = f'INSERT INTO {self.name} ' \
                f'(ticker, date, open, high, low, close, adjusted_close, volume, dividend, split_coefficient) ' \
                f'VALUES {values} ' \
                f'ON CONFLICT DO NOTHING;'
        return self.run_query(query)

    def add_row(self, row):
        return postgres.insert_row_as_dict(self.cursor, self.name, row)

    def get_history(self, ticker, year=None):
        query = f"SELECT * FROM {self.name} WHERE ticker = '{ticker}'"
        if year is not None:
            query += f" AND date >= '{year}-01-01' AND date <= '{year}-12-31'"
        query += ' ORDER BY DATE desc'
        postgres.run_query(self.cursor, query)
        return self.cursor.fetchall()
