from database_updaters.calculations import daily_history_calculations
from databases.stocks_database import StocksDatabase

# Note: Relies on existing real data

db = StocksDatabase()


def test_calculate_adjusted_dividends():
    daily_history_rows = db.daily_history_table.get_history('KO')
    rows = daily_history_calculations.calculate_adjusted_dividends(daily_history_rows)
    assert len(rows) > 0
