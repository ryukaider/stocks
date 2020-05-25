from databases import postgres
from databases.database import Database


class Table:

    def __init__(self, table_name, database_name, columns=None):
        self.database = Database(database_name)
        self.cursor = self.database.get_cursor()
        self.table_name = table_name
        self.columns = columns
        self.create()

    def exists(self):
        return postgres.table_exists(self.cursor, self.table_name)

    def create(self):
        if not self.exists():
            return postgres.create_table(self.cursor, self.table_name, self.columns)
        return self.exists()

    def add_column(self, column_name, column_type='varchar'):
        return postgres.add_column(self.cursor, self.table_name, column_name, column_type)

    def delete_column(self, column):
        return postgres.delete_column(self.cursor, self.table_name, column)

    def insert_row(self, dictionary):
        return postgres.insert_row_as_dict(self.cursor, self.table_name, dictionary)

    def get_value(self, key_column, key_value, value_column):
        if isinstance(key_value, str):
            key_value = f"('{key_value}')"
        query = f"SELECT {value_column} FROM {self.table_name} WHERE {key_column} = {key_value}"
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
            self.cursor, self.table_name, key_column, key_value, update_column, update_value)

    def run_query(self, query):
        success = postgres.run_query(self.cursor, query)
        try:
            results = self.cursor.fetchall()
        except Exception:
            return success
        if len(results) == 1:
            return results[0]
        return results
