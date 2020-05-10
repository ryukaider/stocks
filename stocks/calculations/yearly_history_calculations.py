import datetime
from databases.tables.monthly_history_table import MonthlyHistoryTable
from databases.tables.yearly_history_table import YearlyHistoryTable

monthly_history_table = MonthlyHistoryTable()
yearly_history_table = YearlyHistoryTable()


def calculate_end_of_year_price(ticker):
    data = monthly_history_table.get_history(ticker)
    prices = {}
    current_year = datetime.datetime.now().year
    index_year = current_year
    for row in data:
        row_year = row['date'].year
        if row_year == current_year:
            continue
        if row_year != index_year:
            prices[row_year] = round(row['price'], 2)
            index_year = row_year
            continue
    return prices


def calculate_average_price(ticker):
    data = monthly_history_table.get_history(ticker)
    average_prices = {}
    current_year = datetime.datetime.now().year
    index_year = current_year
    index_price = 0
    index_count = 0
    for row in data:
        row_year = row['date'].year
        index_count += 1
        if row_year == index_year:
            index_price += row['price']
            if data.index(row) != (len(data) - 1):
                continue
        average = round((index_price / index_count), 2)
        average_prices[index_year] = average
        index_price = row['price']
        index_count = 1
        index_year = row_year
    return average_prices


def calculate_dividend(ticker):
    data = monthly_history_table.get_date_dividend(ticker)
    dividends = {}
    current_year = datetime.datetime.now().year
    index_year = 0
    dividend = 0
    for row in data:
        row_year = row['date'].year
        if row_year == current_year:
            continue
        if index_year == 0:
            index_year = row_year
        if row_year == index_year:
            dividend += row['dividend']
            continue
        dividends[index_year] = round(dividend, 2)
        index_year = row_year
        dividend = 0
    return dividends


def calculate_dividend_yield(ticker):
    data = yearly_history_table.get_data(ticker)
    dividend_yields = {}
    for row in data:
        try:
            average_share_price = row['average_price']
            dividend = row['dividend']
            dividend_yield = round((dividend / average_share_price) * 100, 2)
            dividend_yields[row['year']] = dividend_yield
        except Exception:
            continue
    return dividend_yields
