# Data provided for free by financialmodelingprep.com
# https://financialmodelingprep.com/terms-of-service

import requests

base_url = 'https://financialmodelingprep.com/api/v3'


def get_company_profile(ticker):
    url = f'{base_url}/company/profile/{ticker}'
    print(url)
    try:
        profile = requests.get(url).json()['profile']
        return profile
    except KeyError:
        return None


def get_daily_price(ticker):
    url = f'{base_url}/historical-price-full/{ticker}?serietype=line'
    print(url)
    try:
        historical_data = requests.get(url).json()['historical']
        return historical_data
    except KeyError:
        return None
