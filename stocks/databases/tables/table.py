from databases import postgres
from databases.database import Database
from config import database_config


class Table:

    def __init__(self, table_name, database_name=database_config.database):
        self.database = Database(database_name)
        self.cursor = self.database.get_cursor()
        self.table_name = table_name
        self.columns = None
        self.create()

    def exists(self):
        return postgres.table_exists(self.cursor, self.table_name)

    def create(self):
        if not self.exists():
            return postgres.create_table(self.cursor, self.table_name, self.columns)
        return self.exists()
