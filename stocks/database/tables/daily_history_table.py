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
        'adjusted_dividend': 'numeric (10, 4)',
        'split_coefficient': 'numeric (10, 4)',
        'UNIQUE': '(ticker, date)'
    }

    def __init__(self, cursor, name='daily_history'):
        Table.__init__(self, cursor, name, self.columns)

    def upsert_rows(self, rows: list):
        """
        Assumes all rows have the same set of keys (columns).
        """

        if rows is None:
            return False

        columns_list = self._get_column_list(rows)
        columns_text = self._get_column_text(columns_list)
        values_text = self._get_values_text(rows, columns_list)
        on_conflict_query = self._get_conflict_update_query(columns_list)

        query = f'INSERT INTO {self.name} ' \
                f'({columns_text}) ' \
                f'VALUES {values_text} ' \
                f'ON CONFLICT (ticker, date) DO UPDATE {on_conflict_query};'
        return self.run_query(query)

    @staticmethod
    def _get_column_list(rows):
        columns_list = []
        for (column, value) in rows[0].items():
            columns_list.append(column)
        return columns_list

    @staticmethod
    def _get_column_text(columns_list):
        columns_text = ''
        for column in columns_list:
            columns_text += f'{column},'
        columns_text = columns_text.strip(',')
        return columns_text

    @staticmethod
    def _get_values_text(rows, columns_list):
        values = ''
        for row in rows:
            values += '('
            for column in columns_list:
                values += f"'{row[column]}',"
            values = values.strip(',')
            values += '),'
        values = values.strip(',')
        return values

    def _get_conflict_update_query(self, columns: list):
        query = f'SET '
        for column in columns:
            if column == 'ticker' or column == 'date':
                continue
            query += f'{column} = EXCLUDED.{column},'
        query = query.strip(',')
        query += f' WHERE {self.name}.ticker = EXCLUDED.ticker AND {self.name}.date = EXCLUDED.date'
        return query

    def get_history(self, ticker, year=None, orderby='DATE DESC'):
        query = f"SELECT * FROM {self.name} WHERE ticker = '{ticker}'"
        if year is not None:
            query += f" AND date >= '{year}-01-01' AND date <= '{year}-12-31'"
        query += f' ORDER BY {orderby};'
        return self.run_query(query)
