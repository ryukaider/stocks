from database.stocks_database import StocksDatabase
from .api_progress.api_progress_updater import ApiProgressUpdater
from .company_profile.company_profile_updater import CompanyProfileUpdater
from .daily_history.daily_history_updater import DailyHistoryUpdater
from .tickers.tickers_updater import TickersUpdater
from .yearly_history.yearly_history_updater import YearlyHistoryUpdater
from .dividends.dividends_updater import DividendsUpdater


class DatabaseUpdater:
    def __init__(self, database: StocksDatabase):
        self.db = database

        self.api_progress = ApiProgressUpdater(self.db)
        self.company_profile = CompanyProfileUpdater(self.db)
        self.daily_history = DailyHistoryUpdater(self.db)
        self.dividends = DividendsUpdater(self.db)
        self.tickers = TickersUpdater(self.db)
        self.yearly_history = YearlyHistoryUpdater(self.db)

    def update_all(self):
        # First, get the latest tickers from the Nasdaq ftp site
        self.tickers.update_all_tickers(days_old=1)

        # Add any missing tickers to the api_progress table, and remove delisted tickers
        self.api_progress.update_all_tickers()

        # Update basic company info for all tickers last updated more than 30 days ago
        self.company_profile.update_all(days_old=30)

        # Get the latest daily history using APIs
        self.daily_history.update_all(days_old=7)

        # Using the collected daily history, calculate the yearly history
        self.yearly_history.update_all()

        # Next, update dividend information with the yearly history data
        self.dividends.update_all()
