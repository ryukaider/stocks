from database_updaters.daily_history.helpers.status import Status
from database.stocks_database import StocksDatabase
from web_apis import alpha_vantage


class AlphaVantageToDailyHistory:
    def __init__(self, database: StocksDatabase):
        self.db = database

    def update_stock(self, ticker):
        json_data = alpha_vantage.get_daily_history(ticker)
        status = self._get_response_status(json_data)
        if status == Status.Success:
            try:
                self._update_database(ticker, json_data)
            except Exception:
                return Status.Failed
        return status

    def _get_response_status(self, response_json):
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

    def _update_database(self, ticker, json_data):
        daily_history = json_data['Time Series (Daily)']
        rows = []
        for day in daily_history:
            day_data = daily_history[day]
            row = self._format_data(ticker, day, day_data)
            rows.append(row)
        self.db.daily_history_table._upsert_rows(rows)

    def _format_data(self, ticker, day, day_data):
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
