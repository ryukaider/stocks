from database_updaters.calculations import daily_history_calculations

# Note: Relies on existing real data


def test_calculate_adjusted_dividends():
    rows = daily_history_calculations.calculate_adjusted_dividends('KO')
    assert len(rows) > 0
