from databases.tables.api_progress_table import ApiProgressTable
from databases.tables.company_profile_table import CompanyProfileTable
from web_apis import iex
from databases.database import Database
from config import database_config

db = Database(database_config.database)
cursor = db.cursor()

api_progress_table = ApiProgressTable(cursor)
company_profile_table = CompanyProfileTable(cursor)


def update_all_stocks():
    tickers = api_progress_table.get_company_profile_progress(days_old=30)
    for ticker in tickers:
        company_profile_table.add_stock(ticker)
        update_stock(ticker)
        api_progress_table.update_company_profile_progress(ticker)


def update_stock(ticker):
    profile = iex.get_company_profile(ticker)
    if profile is None:
        return False

    company_profile_table.update_name(ticker, profile['companyName'])
    company_profile_table.update_exchange(ticker, profile['exchange'])
    company_profile_table.update_sector(ticker, profile['sector'])
    company_profile_table.update_industry(ticker, profile['industry'])
    company_profile_table.update_description(ticker, profile['description'])
    company_profile_table.update_ceo(ticker, profile['CEO'])
    company_profile_table.update_employees(ticker, profile['employees'])
    company_profile_table.update_website(ticker, profile['website'])
    company_profile_table.update_country(ticker, profile['country'])
    return True


if __name__ == "__main__":
    update_all_stocks()
