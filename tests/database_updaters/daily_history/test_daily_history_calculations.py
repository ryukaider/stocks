from database_updaters.daily_history.adjusted_dividends_calculator import AdjustedDividendsCalculator
from database.stocks_database import StocksDatabase

# Note: Relies on existing real data

db = StocksDatabase()
adjusted_dividends_calculator = AdjustedDividendsCalculator()


def test_calculate_adjusted_dividends():
    daily_history_rows = db.daily_history_table.get_history('KO')
    rows = adjusted_dividends_calculator.calculate(daily_history_rows)
    assert len(rows) > 0
