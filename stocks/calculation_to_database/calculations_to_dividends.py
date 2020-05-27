import datetime
from databases.tables.daily_history_table import DailyHistoryTable
from databases.tables.dividends_table import DividendsTable
from databases.tables.tickers_table import TickersTable
from databases.tables.yearly_history_table import YearlyHistoryTable

daily_history_table = DailyHistoryTable()
dividends_table = DividendsTable()
tickers_table = TickersTable()
yearly_history_table = YearlyHistoryTable()


def update_all_stocks():
    update_dividend_years()
    update_dividend_years_stable()
    update_dividend_years_increasing()
    update_dividend_ttm()
    update_dividend_yield_ttm()


def update_dividend_years():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        dividends_table.add_stock(ticker)
        dividend_years = calculate_dividend_years(ticker)
        dividends_table.update_dividend_years(ticker, dividend_years)


def calculate_dividend_years(ticker):
    data = yearly_history_table.get_data(ticker)
    years = 0
    for row in data:
        if row['dividend'] is None and years == 0:
            continue
        if row['dividend'] is None:
            break
        if row['dividend'] > 0:
            years += 1
        else:
            break
    return years


def update_dividend_years_stable():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        dividends_table.add_stock(ticker)
        dividend_years_stable = calculate_dividend_years_stable(ticker)
        dividends_table.update_dividend_years_stable(ticker, dividend_years_stable)


def calculate_dividend_years_stable(ticker):
    data = yearly_history_table.get_data(ticker)
    years = 0
    previous_year_dividend = None
    for row in data:
        if row['dividend'] is None and years == 0:
            continue
        if row['dividend'] is None:
            break
        if row['dividend'] > 0 and (previous_year_dividend is None or previous_year_dividend >= row['dividend']):
            years += 1
            previous_year_dividend = row['dividend']
        else:
            break
    return years


def update_dividend_years_increasing():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        dividends_table.add_stock(ticker)
        dividend_years_increasing = calculate_years_of_dividends_increasing(ticker)
        dividends_table.update_dividend_years_increasing(ticker, dividend_years_increasing)


def calculate_years_of_dividends_increasing(ticker):
    data = yearly_history_table.get_data(ticker)
    years = 0
    previous_year_dividend = None
    for row in data:
        if row['dividend'] is None and years == 0:
            continue
        if row['dividend'] is None:
            break
        if row['dividend'] > 0 and (previous_year_dividend is None or previous_year_dividend > row['dividend']):
            years += 1
            previous_year_dividend = row['dividend']
        else:
            break
    return years


def update_dividend_yield_ttm():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        dividends_table.add_stock(ticker)
        dividend_yield_ttm = calculate_dividend_yield_ttm(ticker)
        dividends_table.update_dividend_yield_ttm(ticker, dividend_yield_ttm)


def calculate_dividend_yield_ttm(ticker):
    history = daily_history_table.get_history(ticker)
    dividend_yield_ttm = 0
    try:
        latest_price = history[0]['adjusted_close']
        dividend_ttm = dividends_table.get_dividend_ttm(ticker)
        dividend_yield_ttm = (float(dividend_ttm) / float(latest_price)) * 100
    except Exception:
        pass
    return dividend_yield_ttm


def update_dividend_ttm():
    tickers = tickers_table.get_tickers()
    for ticker in tickers:
        dividends_table.add_stock(ticker)
        dividend_ttm = calculate_dividend_ttm(ticker)
        dividends_table.update_dividend_ttm(ticker, dividend_ttm)


def calculate_dividend_ttm(ticker):
    start_date = (datetime.datetime.now() - datetime.timedelta(days=365)).date()
    query = f"SELECT dividend FROM {daily_history_table.table_name} " \
            f"WHERE ticker = '{ticker}' " \
            f"AND date >= '{start_date}' " \
            f"AND dividend != 0"
    rows = daily_history_table.run_query(query)
    dividend_ttm = 0
    for row in rows:
        dividend_ttm += row['dividend']
    return dividend_ttm


if __name__ == "__main__":
    update_all_stocks()
