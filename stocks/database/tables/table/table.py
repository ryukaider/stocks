from .helpers.upsert import Upsert
from database import postgres


class Table:

    def __init__(self, cursor, name, columns=None):
        self.cursor = cursor
        self.name = name
        self.columns: dict = columns
        self.create()

    def exists(self):
        return postgres.table_exists(self.cursor, self.name)

    def create(self):
        if self.exists():
            return self.add_missing_columns()
        else:
            return postgres.create_table(self.cursor, self.name, self.columns)

    def add_missing_columns(self):
        for (column_name, column_type) in self.columns.items():
            self.add_column(column_name, column_type)
        return True

    def add_column(self, column_name, column_type='varchar'):
        return postgres.add_column(self.cursor, self.name, column_name, column_type)

    def delete_column(self, column):
        return postgres.delete_column(self.cursor, self.name, column)

    def insert_row(self, dictionary):
        return postgres.insert_row_as_dict(self.cursor, self.name, dictionary)

    def _upsert_rows(self, rows: list, primary_keys: list):
        return Upsert(self).upsert_rows(rows, primary_keys)

    def delete_row(self, column, value):
        return postgres.remove_row(self.cursor, self.name, column, value)

    def delete_all_rows(self):
        query = f'DELETE FROM {self.name}'
        return self.run_query(query)

    def get_all_rows(self):
        query = f'SELECT * FROM {self.name}'
        return self.run_query(query)

    def get_value(self, key_column, key_value, value_column):
        if isinstance(key_value, str):
            key_value = f"('{key_value}')"
        query = f"SELECT {value_column} FROM {self.name} WHERE {key_column} = {key_value}"
        postgres.run_query(self.cursor, query)
        value = postgres.get_list_results(self.cursor)[0]
        return value

    def get_float_value(self, key_column, key_value, value_column):
        try:
            return float(self.get_value(key_column, key_value, value_column))
        except TypeError:
            return None

    def update_value(self, key_column, key_value, update_column, update_value):
        if update_value is None:
            return False
        return postgres.update_value(
            self.cursor, self.name, key_column, key_value, update_column, update_value)

    def run_query(self, query):
        success = postgres.run_query(self.cursor, query)
        try:
            results = self.cursor.fetchall()
        except Exception:
            return success
        return results

    def get_list_results(self):
        return postgres.get_list_results(self.cursor)
