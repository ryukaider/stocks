from database_updaters.api_to_database_table import iex_to_company_profile, alpha_vantage_to_daily_history
from database_updaters.calculation_to_database import calculations_to_dividends, calculations_to_yearly_history
from database_updaters.database_updater import DatabaseUpdater
from databases.stocks_database import StocksDatabase


db = StocksDatabase()
db_updater = DatabaseUpdater(db)


def main():
    print('*** Starting Stocks Data Collection ***')

    # First, get the latest tickers using APIs
    db_updater.nasdaq_to_tickers.update_all_tickers()

    # Add any missing tickers to the api_progress table
    tickers = db.tickers_table.get_tickers()
    db.api_progress_table.add_tickers(tickers)

    # Update basic company info for all the tickers
    iex_to_company_profile.update_all_stocks()

    # Get the latest daily history using APIs
    alpha_vantage_to_daily_history.update_all_stocks()

    # Using the collected daily history, calculate the yearly history
    calculations_to_yearly_history.update_all_stocks()

    # Next, update dividend information with the yearly history data
    calculations_to_dividends.update_all_stocks()


if __name__ == '__main__':
    main()
