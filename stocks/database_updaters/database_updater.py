from database.stocks_database import StocksDatabase
from .api_to_database_table.iex_to_company_profile import IexToCompanyProfile
from .calculation_to_database.calculations_to_api_progress import CalculationsToApiProgress
from .daily_history.daily_history_updater import DailyHistoryUpdater
from .tickers.tickers_updater import TickersUpdater


class DatabaseUpdater:
    def __init__(self, database: StocksDatabase):
        self.db = database

        self.calculations_to_api_progress = CalculationsToApiProgress(self.db)
        self.iex_to_company_profile = IexToCompanyProfile(self.db)

        self.tickers = TickersUpdater(self.db)
        self.daily_history = DailyHistoryUpdater(self.db)
