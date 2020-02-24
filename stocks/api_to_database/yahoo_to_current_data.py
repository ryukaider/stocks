import sys
sys.path.append('E:/Google Drive/Computers/Dev/Stocks/scott_stocks')

from web_apis import yahoo
from database.tables import api_progress
from database.tables import current_data

def add_all_eps_ttm():
    tickers = api_progress.get_incomplete_stocks('eps')
    for ticker in tickers:
        add_eps_ttm(ticker)

def add_eps_ttm(ticker):
    eps = yahoo.get_eps_ttm(ticker)
    if eps == None or current_data.update_eps_ttm(ticker, eps):
        api_progress.set_eps_done(ticker)

if __name__ == "__main__":
    add_all_eps_ttm()
