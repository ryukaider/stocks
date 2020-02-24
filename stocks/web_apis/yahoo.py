import sys
sys.path.append('E:/Google Drive/Computers/Dev/Stocks/scott_stocks')

import requests
import json
from database.tables import current_data

base_url = 'https://finance.yahoo.com/quote/'

def get_summary_data(ticker):
    query = base_url + ticker
    print(query)
    try:
        response = requests.get(query)
        print(response)
        if response.status_code != 200:
            return None
        return response.text
    except Exception as error:
        print(error)
        return None

def get_eps_ttm(ticker):
    data = get_summary_data(ticker)
    if data == None:
        return None
    eps = _get_eps_ttm_from_response(data)
    return eps

def _get_eps_ttm_from_response(response):
    key = 'EPS (TTM)'
    end_text = '</span></td></tr>'
    splitText = response.split(key)[1]
    splitText = splitText.split(end_text)[0]
    eps = splitText.split('">')[-1]
    if _is_number(eps):
        return eps
    else:
        return None

def _is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    print(get_eps_ttm('MMM'))
