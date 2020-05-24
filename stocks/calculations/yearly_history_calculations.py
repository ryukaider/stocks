import datetime
from databases.tables.daily_history_table import DailyHistoryTable
from databases.tables.yearly_history_table import YearlyHistoryTable

daily_history_table = DailyHistoryTable()
yearly_history_table = YearlyHistoryTable()


def calculate_end_of_year_prices(ticker, start_year=2000):
    yearly_prices = {}
    current_year = datetime.datetime.now().year
    for year in range(start_year, current_year):
        price = calculate_end_of_year_price(ticker, year)
        yearly_prices[year] = price
    return yearly_prices


def calculate_end_of_year_price(ticker, year):
    query = f"SELECT adjusted_close " \
            f"FROM {daily_history_table.table_name} " \
            f"WHERE ticker = '{ticker}' " \
            f"AND date >= '{year}-01-01' " \
            f"AND date <= '{year}-12-31' " \
            f"ORDER BY date desc " \
            f"LIMIT 1"
    result = daily_history_table.run_query(query)
    return result[0]


def calculate_average_price(ticker):
    data = daily_history_table.get_history(ticker)
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
    data = daily_history_table.get_history(ticker)
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
