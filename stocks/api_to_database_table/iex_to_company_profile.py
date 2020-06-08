from config import database_config
from databases.stocks_database import StocksDatabase
from web_apis import iex

db = StocksDatabase(database_config.database)


def update_all_stocks():
    tickers = db.api_progress_table.get_company_profile_progress(days_old=30)
    for ticker in tickers:
        db.company_profile_table.add_stock(ticker)
        update_stock(ticker)
        db.api_progress_table.update_company_profile_progress(ticker)


def update_stock(ticker):
    profile = iex.get_company_profile(ticker)
    if profile is None:
        return False

    db.company_profile_table.update_name(ticker, profile['companyName'])
    db.company_profile_table.update_exchange(ticker, profile['exchange'])
    db.company_profile_table.update_sector(ticker, profile['sector'])
    db.company_profile_table.update_industry(ticker, profile['industry'])
    db.company_profile_table.update_description(ticker, profile['description'])
    db.company_profile_table.update_ceo(ticker, profile['CEO'])
    db.company_profile_table.update_employees(ticker, profile['employees'])
    db.company_profile_table.update_website(ticker, profile['website'])
    db.company_profile_table.update_country(ticker, profile['country'])
    return True


if __name__ == "__main__":
    update_all_stocks()
