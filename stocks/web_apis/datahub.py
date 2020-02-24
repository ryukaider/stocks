import requests

base_url = 'https://datahub.io/core/'

def get_stocks_ticker_name_exchange():
    print("Getting stock names from datahub.io")
    stocks = []
    stocks.extend(get_nyse_stock_names())
    stocks.extend(get_nasdaq_stock_names())
    return stocks

def get_nyse_stock_names():
    print("Getting NYSE stock names")
    response = requests.get(f'{base_url}nyse-other-listings/r/nyse-listed.json')
    stocks = []
    for stockdata in response.json():
        stock = {
            "exchange": "NYSE",
            "ticker": stockdata["ACT Symbol"],
            "name": stockdata["Company Name"]
        }
        stocks.append(stock)
    return stocks

def get_nasdaq_stock_names():
    print("Getting NASDAQ stock names")
    response = requests.get("https://datahub.io/core/nasdaq-listings/r/nasdaq-listed-symbols.json")
    stocks = []
    for stockdata in response.json():
        stock = {
            "exchange": "NASDAQ",
            "ticker": stockdata["Symbol"],
            "name": stockdata["Company Name"]
        }
        stocks.append(stock)
    return stocks
