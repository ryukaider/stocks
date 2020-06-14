import requests
from config import keys_config

base_url = 'https://www.alphavantage.co/query?'
api_key = keys_config.alpha_vantage_api_key


def get_daily_history(ticker):
    function = 'TIME_SERIES_DAILY_ADJUSTED'
    query_filter = '&outputsize=full'
    return _get_response(function, ticker, query_filter)


def get_monthly_history(ticker):
    function = 'TIME_SERIES_MONTHLY_ADJUSTED'
    return _get_response(function, ticker)


def _get_response(function, ticker, query_filter=None):
    print(f'Getting Alpha Vantage {function} for {ticker}')
    query = _get_query(function, ticker, query_filter)
    print(query)
    try:
        response = requests.get(query)
        return response.json()
    except Exception as error:
        print(error)
        return None


def _get_query(function, ticker, query_filter=None):
    return f'{base_url}function={function}&symbol={ticker}&apikey={api_key}{query_filter}'


if __name__ == '__main__':
    get_daily_history('ABR-A')
