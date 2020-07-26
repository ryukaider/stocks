from database.stocks_database import StocksDatabase
from database_updaters.database_updater import DatabaseUpdater

print('*** Starting Stocks Data Collection ***')

db = StocksDatabase()
db_updater = DatabaseUpdater(db)

#db_updater.update_all()
db_updater.company_profile.update_all(days_old=1)
