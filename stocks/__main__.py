from database.stocks_database import StocksDatabase
from database_updaters.database_updater import DatabaseUpdater

print('*** Starting Stocks Data Collection ***')

db = StocksDatabase()
db_updater = DatabaseUpdater(db)

db_updater.update_all()
