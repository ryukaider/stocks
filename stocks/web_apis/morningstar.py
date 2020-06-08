import requests
from config import database_config
from databases.database import Database
from databases.tables.current_data_table import CurrentDataTable

base_url = 'https://www.morningstar.com/stocks/'

db = Database(database_config.database)
current_data_table = CurrentDataTable(db.cursor())


def get_financial_data(ticker):
    function = 'financials'
    exchange = current_data_table.get_exchange(ticker)
    exchange = _convert_exchange(exchange)
    ticker = ticker.lower()
    query = _get_query(exchange, ticker, function)
    print(query)
    try:
        response = requests.get(query)
        print(response.content)
        print(response)
        return response.content
    except Exception as error:
        print(error)
        return None


def _get_query(exchange, ticker, function):
    query = f'{base_url}{exchange}/{ticker}/{function}'
    return query


def _convert_exchange(exchange):
    if exchange.lower() == 'nyse':
        return 'xnys'
    if exchange.lower() == 'nasdaq':
        return 'xnas'
    return exchange


if __name__ == "__main__":
    get_financial_data('MMM')
