from databases.tables.tickers_table import TickersTable
from databases.tables.company_profile_table import CompanyProfileTable
from web_apis import iex

tickers_table = TickersTable()
company_profile_table = CompanyProfileTable()


def update_all_stocks():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        company_profile_table.add_stock(ticker)
        update_stock(ticker)


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