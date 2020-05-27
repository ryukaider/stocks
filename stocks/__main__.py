from api_to_database_table import alpha_vantage_to_daily_history
from api_to_database_table import datahub_to_tickers
from api_to_database_table import iex_to_company_profile
from calculation_to_database import calculations_to_yearly_history
from databases.tables.api_progress_table import ApiProgressTable


def main():
    print('*** Starting Stocks Data Collection ***')

    # First, get the latest tickers using APIs
    #datahub_to_tickers.update_tickers()
    #ApiProgressTable().reset_all()

    # Get basic company info for all the tickers
    #iex_to_company_profile.update_all_stocks()

    # Get the latest daily history using APIs
    alpha_vantage_to_daily_history.update_all_stocks()

    # Using the collected daily history, calculate the yearly history
    calculations_to_yearly_history.update_all_stocks()


if __name__ == '__main__':
    main()
