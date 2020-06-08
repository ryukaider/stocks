import time
from api_to_database_table.helpers.status import Status
from config import database_config
from databases.stocks_database import StocksDatabase
from web_apis import alpha_vantage

db = StocksDatabase(database_config.database)


def update_all_stocks():
    tickers = db.api_progress_table.get_daily_history_progress(days_old=7)
    for ticker in tickers:
        status = update_stock(ticker)
        print(status)
        if status == Status.Success or status == Status.Invalid:
            db.api_progress_table.update_daily_history_progress(ticker)
            time.sleep(15)  # API limits 5 calls per minute
            continue
        if status == Status.Failed:
            continue
        if status == Status.API_Limit:
            print('Stopping due to reaching APi limit')
            break


def update_stock(ticker):
    raw_data = alpha_vantage.get_daily_history(ticker)
    status = _get_response_status(raw_data)
    if status == Status.Success:
        daily_history = raw_data['Time Series (Daily)']
        for day in daily_history:
            day_data = daily_history[day]
            row = _format_data(ticker, day, day_data)
            daily_history_table.add_row(row)
    return status


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
    update_all_stocks()
