from databases.database import Database
from databases.tables.api_progress_table import ApiProgressTable
from databases.tables.tickers_table import TickersTable


class StocksDatabase(Database):
    def __init__(self, name):
        Database.__init__(self, name)
        self.name = name
        self.tickers_table = TickersTable(database_name=name)
        self.api_progress_table = ApiProgressTable(database_name=name)
