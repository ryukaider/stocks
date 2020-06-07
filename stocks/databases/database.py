import psycopg2.extras
from config import database_config
from config import keys_config
from databases import postgres


class Database:

    def __init__(self, name):
        self.name = name
        self.create()

    def exists(self):
        cursor = self.get_cursor(with_database=False)
        return postgres.database_exists(cursor, self.name)

    def create(self):
        cursor = self.get_cursor(with_database=False)
        if not self.exists():
            return postgres.create_database(cursor, self.name)
        return cursor is not None

    def get_cursor(self, with_database=True):
        connection = self.get_connection(with_database)
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return cursor

    def get_connection(self, with_database=True):
        database_name = self.name if with_database else None
        return postgres.connect(
            database_config.username,
            keys_config.database_password,
            database_config.host,
            database_config.port,
            database_name)
