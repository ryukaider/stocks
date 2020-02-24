import sys
sys.path.append('E:/Google Drive/Computers/Dev/Stocks/scott_stocks')

import datetime
from database.tables import yearly_history
from database.tables import monthly_history
from database.tables import current_data

def calculate_dividend_ttm(ticker):
    dividends = monthly_history.get_dividend_ttm(ticker)
    annual_dividend = 0
    for dividend in dividends:
        annual_dividend += dividend
    print(f'{ticker} annual dividend = ${annual_dividend} per share')
    return annual_dividend

def calculate_dividend_yield(ticker):
    dividend = current_data.get_dividend_ttm(ticker)
    price = current_data.get_price(ticker)
    try:
        dividend_yield = (dividend / price) * 100
        return dividend_yield
    except:
        return None

def calculate_years_of_dividends(ticker):
    data = yearly_history.get_data(ticker)
    years = 0
    for row in data:
        if row['dividend'] == None and years == 0:
            continue
        if row['dividend'] == None:
            break
        if row['dividend'] > 0:
            years += 1
        else:
            break
    return years

def calculate_years_of_dividends_increasing(ticker):
    data = yearly_history.get_data(ticker)
    years = 0
    previous_year_dividend = None
    for row in data:
        if row['dividend'] == None and years == 0:
            continue
        if row['dividend'] == None:
            break
        if row['dividend'] > 0 and (previous_year_dividend == None or previous_year_dividend > row['dividend']):
            years += 1
            previous_year_dividend = row['dividend']
        else:
            break
    return years

def calculate_payout_ratio_ttm(ticker):
    dividend_ttm = current_data.get_dividend_ttm(ticker)
    eps_ttm = current_data.get_eps_ttm(ticker)
    if dividend_ttm == None or eps_ttm == None or eps_ttm == 0:
        return None
    payout_ratio_ttm = (dividend_ttm / eps_ttm)
    payout_ratio_ttm_percent = payout_ratio_ttm * 100
    payout_ratio_ttm_percent_rounded = round( payout_ratio_ttm_percent, 2)
    return payout_ratio_ttm_percent_rounded

if __name__ == "__main__":
    years = calculate_years_of_dividends_increasing('MSFT')
    print(years)
