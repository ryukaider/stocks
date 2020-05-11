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
