from database.stocks_database import StocksDatabase
from .api_progress.api_progress_updater import ApiProgressUpdater
from .company_profile.company_profile_updater import CompanyProfileUpdater
from .daily_history.daily_history_updater import DailyHistoryUpdater
from .tickers.tickers_updater import TickersUpdater


class DatabaseUpdater:
    def __init__(self, database: StocksDatabase):
        self.db = database

        self.api_progress = ApiProgressUpdater(self.db)
        self.company_profile = CompanyProfileUpdater(self.db)
        self.daily_history = DailyHistoryUpdater(self.db)
        self.tickers = TickersUpdater(self.db)
