from database import postgres
from database import stocks_database


class Table:

    def __init__(self, table_name):
        self.cursor = stocks_database.get_cursor()
        self.table_name = table_name
        self.columns = None
        self.create()

    def exists(self):
        return postgres.table_exists(self.cursor, self.table_name)

    def create(self):
        if not self.exists():
            return postgres.create_table(self.cursor, self.table_name, self.columns)
        return self.exists()
