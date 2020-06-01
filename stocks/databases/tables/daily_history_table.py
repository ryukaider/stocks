from config import database_config
from databases import postgres
from databases.tables.table import Table


class DailyHistoryTable(Table):
    columns = {
        'ticker': 'text NOT NULL',
        'date': 'date NOT NULL',
        'open': 'numeric (10, 2)',
        'high': 'numeric (10, 2)',
        'low': 'numeric (10, 2)',
        'close': 'numeric (10, 2)',
        'adjusted_close': 'numeric (10, 2)',
        'volume': 'integer',
        'dividend': 'numeric (10, 2)',
        'split_coefficient': 'numeric (10, 4)',
        'UNIQUE': '(ticker, date)'
    }

    def __init__(self,
                 name='daily_history',
                 database_name=database_config.database):
        Table.__init__(self, name, database_name, self.columns)

    def add_row(self, row):
        return postgres.insert_row_as_dict(self.cursor, self.name, row)

    def get_history(self, ticker, year=None):
        query = f"SELECT * FROM {self.name} WHERE ticker = '{ticker}'"
        if year is not None:
            query += f" AND date >= '{year}-01-01' AND date <= '{year}-12-31'"
        query += ' ORDER BY DATE desc'
        postgres.run_query(self.cursor, query)
        return self.cursor.fetchall()
