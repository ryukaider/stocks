from api_to_database_table import alpha_vantage_to_daily_history
from api_to_database_table import iex_to_company_profile
from calculation_to_database import calculations_to_yearly_history
from databases.stocks_database import StocksDatabase
from databases.tables.api_progress_table import ApiProgressTable
from web_apis import nasdaq


db = StocksDatabase('stocks')
api_progress_table = ApiProgressTable()


def main():
    print('*** Starting Stocks Data Collection ***')

    # First, get the latest tickers using APIs
    db.tickers_table.delete_all_rows()
    tickers = nasdaq.get_all_tickers()
    db.tickers_table.add_tickers(tickers)

    # Add any missing tickers to the api_progress table
    api_progress_table.add_tickers(tickers)

    # Get basic company info for all the tickers
    iex_to_company_profile.update_all_stocks()

    # Get the latest daily history using APIs
    alpha_vantage_to_daily_history.update_all_stocks()

    # Using the collected daily history, calculate the yearly history
    calculations_to_yearly_history.update_all_stocks()


if __name__ == '__main__':
    main()
