from databases.tables.api_progress_table import ApiProgressTable
from databases.tables.current_data_table import CurrentDataTable
from web_apis import yahoo
from databases.database import Database
from config import database_config

db = Database(database_config.database)
cursor = db.cursor()

api_progress_table = ApiProgressTable(cursor)
current_data_table = CurrentDataTable(cursor)


def add_all_eps_ttm():
    tickers = api_progress_table.get_incomplete_stocks('eps')
    for ticker in tickers:
        add_eps_ttm(ticker)


def add_eps_ttm(ticker):
    eps = yahoo.get_eps_ttm(ticker)
    if eps is None or current_data_table.update_eps_ttm(ticker, eps):
        api_progress_table.set_eps_done(ticker)


if __name__ == "__main__":
    add_all_eps_ttm()
