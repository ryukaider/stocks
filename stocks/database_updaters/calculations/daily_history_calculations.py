from databases.stocks_database import StocksDatabase

db = StocksDatabase()


def calculate_adjusted_dividends(ticker: str):
    """
    The adjusted dividend is the dividend adjusted for stock splits
    """

    daily_history_data = db.daily_history_table.get_history(ticker)
    if not _any_splits(daily_history_data) or not _any_dividends(daily_history_data):
        return None

    adjusted_dividend_rows = []
    cumulative_coefficient = 1

    for row in daily_history_data:
        cumulative_coefficient *= row['split_coefficient']
        adjusted_dividend = row['dividend'] / cumulative_coefficient
        adjusted_dividend_row = {
            'ticker': row['ticker'],
            'date': row['date'],
            'adjusted_dividend': adjusted_dividend
        }
        adjusted_dividend_rows.append(adjusted_dividend_row)
    return adjusted_dividend_rows


def _any_splits(daily_history_data):
    for row in daily_history_data:
        if row['split_coefficient'] != 1:
            return True
    return False


def _any_dividends(daily_history_data):
    for row in daily_history_data:
        if row['dividend'] > 0:
            return True
    return False
