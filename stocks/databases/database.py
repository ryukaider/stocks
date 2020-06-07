from config import database_config
from config import keys_config
from databases import postgres


class Database:

    def __init__(self, name):
        self.name = name
        self.create()

    def exists(self):
        cursor = self.cursor(with_database=False)
        return postgres.database_exists(cursor, self.name)

    def create(self):
        cursor = self.cursor(with_database=False)
        if not self.exists():
            return postgres.create_database(cursor, self.name)
        return cursor is not None

    def cursor(self, with_database=True):
        database_name = self.name if with_database else None
        return postgres.cursor(
            database_config.username,
            keys_config.database_password,
            database_config.host,
            database_config.port,
            database_name)
