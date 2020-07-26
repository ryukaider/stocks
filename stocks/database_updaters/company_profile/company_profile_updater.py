from .components.yahoo_company_profile_converter import YahooCompanyProfileConverter
from database.stocks_database import StocksDatabase


class CompanyProfileUpdater:
    def __init__(self, database: StocksDatabase):
        self.db = database
        self.yahoo = YahooCompanyProfileConverter()

    def update_all(self, days_old=30):
        """
        Updates company profile table for all stocks.
        """

        tickers = self.db.api_progress_table.get_company_profile_progress(days_old)
        for ticker in tickers:
            self.update(ticker)

    def update(self, ticker):
        company_profile = self.yahoo.get_company_profile(ticker)

        if company_profile is None:
            return False

        company_profile_dict = vars(company_profile)
        company_profile_rows = [company_profile_dict]

        success = self.db.company_profile_table.upsert(company_profile_rows)

        if success:
            self.db.api_progress_table.update_company_profile_progress(ticker)
        return success
