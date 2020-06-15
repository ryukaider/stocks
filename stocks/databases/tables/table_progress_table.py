import datetime
from databases import postgres
from .table import Table


class TableProgressTable(Table):

    columns = {
        'table_name': 'text PRIMARY KEY NOT NULL',
        'last_updated': 'date'
    }

    def __init__(self, cursor, name='table_progress'):
        Table.__init__(self, cursor, name, self.columns)

    def add_row(self, table_name):
        row = {'table_name': table_name}
        return self.insert_row(row)

    def update_progress(self, table_name, date=datetime.datetime.now().date()):
        return postgres.update_value(self.cursor, self.name, 'table_name', table_name, 'last_updated', date)

    def reset_progress(self, table_name):
        query = f"UPDATE {self.name} SET 'last_updated' = NULL WHERE table_name = '{table_name}'"
        return self.run_query(query)

    def get_last_updated(self, table_name):
        query = f"SELECT last_updated " \
                f"FROM {self.name} " \
                f"WHERE table_name = '{table_name}'"
        rows = self.run_query(query)
        if rows == 0:
            return None
        return rows[0]['last_updated']
