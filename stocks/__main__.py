from database_updaters.calculation_to_database import calculations_to_dividends, calculations_to_yearly_history
from database_updaters.database_updater import DatabaseUpdater
from database.stocks_database import StocksDatabase


db = StocksDatabase()
db_updater = DatabaseUpdater(db)


def main():
    print('*** Starting Stocks Data Collection ***')

    # First, get the latest tickers from the Nasdaq ftp site
    db_updater.tickers.update_all_tickers(days_old=1)

    # Add any missing tickers to the api_progress table, and remove delisted tickers
    db_updater.api_progress.update_all_tickers()

    # Update basic company info for all tickers last updated more than 30 days ago
    db_updater.iex_to_company_profile.update_all_tickers(days_old=30)

    # Get the latest daily history using APIs
    db_updater.daily_history.update_all(days_old=1)

    # Using the collected daily history, calculate the yearly history
    calculations_to_yearly_history.update_all_stocks()

    # Next, update dividend information with the yearly history data
    calculations_to_dividends.update_all_stocks()


if __name__ == '__main__':
    main()
