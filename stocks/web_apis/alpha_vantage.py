import os, sys
root_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root_path)

import requests
from config import keys_config

base_url = 'https://www.alphavantage.co/query?'
api_key = keys_config.alpha_vantage_api_key


def get_monthly_data(ticker):
    print(f'Getting Alpha Vantage monthly data for {ticker}')
    function = 'TIME_SERIES_MONTHLY_ADJUSTED'
    query = get_query(function, ticker)
    print(query)
    try:
        response = requests.get(query)
        print(response)
        return response.json()
    except Exception as error:
        print(error)
        return None


def get_dividend(response):
    dividends = {}
    monthly_data = response['Monthly Adjusted Time Series']
    for month in monthly_data:
        month_data = monthly_data[month]
        dividend = month_data['7. dividend amount']
        dividends[month] = dividend
    return dividends


def get_query(function, ticker):
    return f'{base_url}function={function}&symbol={ticker}&apikey={api_key}'
