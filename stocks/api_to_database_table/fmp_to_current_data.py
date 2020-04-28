import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(_root_path)

from web_apis import financial_modeling_prep as fmp
from database.tables.tickers_table import TickersTable
from database.tables.current_data_table import CurrentDataTable

tickers_table = TickersTable()
current_data_table = CurrentDataTable()


def update_all_profiles():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        current_data_table.add_stock(ticker)
        update_profile(ticker)


def update_profile(ticker):
    profile = fmp.get_company_profile(ticker)
    if profile is None:
        return False

    current_data_table.update_name(ticker, profile['companyName'])
    current_data_table.update_sector(ticker, profile['sector'])
    current_data_table.update_industry(ticker, profile['industry'])
    current_data_table.update_ceo(ticker, profile['ceo'])
    current_data_table.update_website(ticker, profile['website'])
    current_data_table.update_description(ticker, profile['description'])
    current_data_table.update_change(ticker, profile['changes'])
    current_data_table.update_change_percent(ticker, profile['changesPercentage'])
    current_data_table.update_beta(ticker, profile['beta'])
    current_data_table.update_range(ticker, profile['range'])
    current_data_table.update_volume(ticker, profile['volAvg'])
    current_data_table.update_market_cap(ticker, profile['mktCap'])
    current_data_table.update_last_dividend(ticker, profile['lastDiv'])


if __name__ == "__main__":
    update_all_profiles()
