import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(_root_path)

from web_apis import yahoo
from database.tables import api_progress_table
from database.tables import current_data_table


def add_all_eps_ttm():
    tickers = api_progress_table.get_incomplete_stocks('eps')
    for ticker in tickers:
        add_eps_ttm(ticker)


def add_eps_ttm(ticker):
    eps = yahoo.get_eps_ttm(ticker)
    if eps == None or current_data_table.update_eps_ttm(ticker, eps):
        api_progress_table.set_eps_done(ticker)


if __name__ == "__main__":
    add_all_eps_ttm()
