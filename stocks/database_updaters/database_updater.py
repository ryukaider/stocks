from databases.stocks_database import StocksDatabase
from .api_to_database_table.nasdaq_to_tickers import NasdaqToTickers
from .api_to_database_table.iex_to_company_profile import IexToCompanyProfile
from .calculation_to_database.calculations_to_api_progress import CalculationsToApiProgress


class DatabaseUpdater:
    def __init__(self, database: StocksDatabase):
        self.db = database

        self.nasdaq_to_tickers = NasdaqToTickers(self.db)
        self.calculations_to_api_progress = CalculationsToApiProgress(self.db)
        self.iex_to_company_profile = IexToCompanyProfile(self.db)
