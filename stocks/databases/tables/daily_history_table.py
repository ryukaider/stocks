from config import database_config
from databases import postgres
from databases.tables.table import Table


class DailyHistoryTable(Table):
    columns = {
        'ticker': 'text NOT NULL',
        'date': 'date NOT NULL',
        'price': 'double precision',
        'dividend': 'double precision',
        'UNIQUE': '(ticker, date)'
    }

    def __init__(self,
                 table_name='daily_history',
                 database_name=database_config.database):
        Table.__init__(self, table_name, database_name, self.columns)

    def add_row(self, row):
        return postgres.insert_row_as_dict(self.cursor, self.table_name, row)
