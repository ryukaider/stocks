# Data provided for free by financialmodelingprep.com
# https://financialmodelingprep.com/terms-of-service

import requests

base_url = 'https://financialmodelingprep.com/api/v3'


def get_company_profile(ticker):
    url = f'{base_url}/company/profile/{ticker}'
    print(url)
    profile = requests.get(url).json()['profile']
    return profile
