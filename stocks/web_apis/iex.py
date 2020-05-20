import requests
from config import keys_config

base_url = 'https://cloud.iexapis.com/v1'
token = keys_config.iex_cloud_api_key


def get_company_profile(ticker):
    url = f'{base_url}/stock/{ticker}/company?token={token}'
    print(url)
    try:
        return requests.get(url).json()
    except Exception:
        return None
