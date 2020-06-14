from databases.stocks_database import StocksDatabase
from web_apis import iex


class IexToCompanyProfile:
    def __init__(self, database: StocksDatabase):
        self.db = database

    def update_all_stocks(self, days_old=30):
        tickers = self.db.api_progress_table.get_company_profile_progress(days_old)
        for ticker in tickers:
            self.db.company_profile_table.add_stock(ticker)
            success = self.update_stock(ticker)
            if success:
                self.db.api_progress_table.update_company_profile_progress(ticker)
            else:
                self.db.api_progress_table.reset_company_profile_progress(ticker)

    def update_stock(self, ticker):
        profile = iex.get_company_profile(ticker)
        if profile is None:
            return False

        self.db.company_profile_table.update_name(ticker, profile['companyName'])
        self.db.company_profile_table.update_exchange(ticker, profile['exchange'])
        self.db.company_profile_table.update_sector(ticker, profile['sector'])
        self.db.company_profile_table.update_industry(ticker, profile['industry'])
        self.db.company_profile_table.update_description(ticker, profile['description'])
        self.db.company_profile_table.update_ceo(ticker, profile['CEO'])
        self.db.company_profile_table.update_employees(ticker, profile['employees'])
        self.db.company_profile_table.update_website(ticker, profile['website'])
        self.db.company_profile_table.update_country(ticker, profile['country'])
        return True


if __name__ == "__main__":
    db = StocksDatabase()
    IexToCompanyProfile(db).update_all_stocks()
