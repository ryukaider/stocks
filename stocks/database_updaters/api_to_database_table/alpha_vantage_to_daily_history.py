import time
from database_updaters.api_to_database_table.helpers.status import Status
from database.stocks_database import StocksDatabase
from web_apis import alpha_vantage


class AlphaVantageToDailyHistory:
    def __init__(self, database: StocksDatabase):
        self.db = database

    def update_all_stocks(self, days_old=7):
        tickers = self.db.api_progress_table.get_daily_history_progress(days_old)
        for ticker in tickers:
            status = self.update_stock(ticker)
            print(status)
            if status == Status.Success or status == Status.Invalid:
                self.db.api_progress_table.update_daily_history_progress(ticker)
                time.sleep(15)  # API limits 5 calls per minute
                continue
            if status == Status.Failed:
                continue
            if status == Status.API_Limit:
                print('Stopping due to reaching APi limit')
                break

    def update_stock(self, ticker):
        raw_data = alpha_vantage.get_daily_history(ticker)
        status = self._get_response_status(raw_data)
        if status == Status.Success:
            try:
                daily_history = raw_data['Time Series (Daily)']
                rows = []
                for day in daily_history:
                    day_data = daily_history[day]
                    row = self._format_data(ticker, day, day_data)
                    rows.append(row)
                self.db.daily_history_table.upsert_rows(rows)
            except Exception:
                return Status.Failed
        return status

    @staticmethod
    def _get_response_status(response_json):
        try:
            if response_json is None:
                return Status.Failed
            if 'Error Message' in response_json and 'Invalid API call' in response_json['Error Message']:
                return Status.Invalid
            if 'Note' in response_json and '500 calls per day' in response_json['Note']:
                print(response_json)
                return Status.API_Limit
        except Exception:
            return Status.Invalid
        return Status.Success

    @staticmethod
    def _format_data(ticker, day, day_data):
        return {
            'ticker': ticker,
            'date': day,
            'open': day_data['1. open'],
            'high': day_data['2. high'],
            'low': day_data['3. low'],
            'close': day_data['4. close'],
            'adjusted_close': day_data['5. adjusted close'],
            'volume': day_data['6. volume'],
            'dividend': day_data['7. dividend amount'],
            'split_coefficient': day_data['8. split coefficient']
        }


if __name__ == "__main__":
    AlphaVantageToDailyHistory(StocksDatabase()).update_stock('KO')
