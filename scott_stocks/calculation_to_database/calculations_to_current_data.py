import sys
sys.path.append('E:/Google Drive/Computers/Dev/Stocks/scott_stocks')

from database.tables import tickers_table as tickers_table
from database.tables import current_data
from database.tables import monthly_history
from calculations import current_data_calculations

def update_all():
    update_all_latest_price()
    update_all_rolling_annual_dividend()
    update_all_dividend_yield()
    update_all_dividend_years()
    update_all_dividend_years_increasing()
    update_all_payout_ratio_ttm()

def update_all_latest_price():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        update_latest_price(ticker)

def update_latest_price(ticker):
    price = monthly_history.get_latest_price(ticker)
    current_data.update_price(ticker, price)

def update_all_rolling_annual_dividend():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        update_rolling_annual_dividend(ticker)

def update_rolling_annual_dividend(ticker):
    dividend = current_data_calculations.calculate_dividend_ttm(ticker)
    dividend = round(dividend, 2)
    current_data.update_annual_dividend(ticker, dividend)

def update_all_dividend_yield():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        update_dividend_yield(ticker)
    
def update_dividend_yield(ticker):
    dividend_yield = current_data_calculations.calculate_dividend_yield(ticker)
    current_data.update_dividend_yield(ticker, dividend_yield)

def update_all_dividend_years():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        update_dividend_years(ticker)
    
def update_dividend_years(ticker):
    dividend_years = current_data_calculations.calculate_years_of_dividends(ticker)
    current_data.update_dividend_years(ticker, dividend_years)

def update_all_dividend_years_increasing():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        update_dividend_years_increasing(ticker)
    
def update_dividend_years_increasing(ticker):
    dividend_increasing_years = current_data_calculations.calculate_years_of_dividends_increasing(ticker)
    current_data.update_dividend_years_increasing(ticker, dividend_increasing_years)

def update_all_payout_ratio_ttm():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        update_payout_ratio_ttm(ticker)

def update_payout_ratio_ttm(ticker):
    payout_ratio_ttm = current_data_calculations.calculate_payout_ratio_ttm(ticker)
    current_data.update_payout_ratio_ttm(ticker, payout_ratio_ttm)

if __name__ == "__main__":
    #update_all()
    update_all_payout_ratio_ttm()
