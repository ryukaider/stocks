class AdjustedDividendsCalculator:

    def calculate(self, daily_history_rows):
        """
        The adjusted dividend is the dividend adjusted for stock splits
        """

        if not self._any_splits(daily_history_rows) or not self._any_dividends(daily_history_rows):
            return None

        adjusted_dividend_rows = []
        cumulative_coefficient = 1

        for row in daily_history_rows:
            cumulative_coefficient *= row['split_coefficient']
            adjusted_dividend = row['dividend'] / cumulative_coefficient
            adjusted_dividend_row = {
                'ticker': row['ticker'],
                'date': row['date'],
                'adjusted_dividend': adjusted_dividend
            }
            adjusted_dividend_rows.append(adjusted_dividend_row)
        return adjusted_dividend_rows


    def _any_splits(self, daily_history_data):
        for row in daily_history_data:
            if row['split_coefficient'] != 1:
                return True
        return False


    def _any_dividends(self, daily_history_data):
        for row in daily_history_data:
            if row['dividend'] > 0:
                return True
        return False
