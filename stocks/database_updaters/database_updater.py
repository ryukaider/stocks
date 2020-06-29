from database.stocks_database import StocksDatabase
from .api_to_database_table.iex_to_company_profile import IexToCompanyProfile
from .api_progress.api_progress_updater import ApiProgressUpdater
from .daily_history.daily_history_updater import DailyHistoryUpdater
from .tickers.tickers_updater import TickersUpdater


class DatabaseUpdater:
    def __init__(self, database: StocksDatabase):
        self.db = database

        self.iex_to_company_profile = IexToCompanyProfile(self.db)

        self.tickers = TickersUpdater(self.db)
        self.api_progress = ApiProgressUpdater(self.db)
        self.daily_history = DailyHistoryUpdater(self.db)
