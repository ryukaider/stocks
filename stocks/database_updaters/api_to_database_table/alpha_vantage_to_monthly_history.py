import time
from database_updaters.api_to_database_table.helpers.status import Status
from database.stocks_database import StocksDatabase
from web_apis import alpha_vantage

db = StocksDatabase()


def update_all():
    tickers = db.api_progress_table.get_incomplete_stocks('monthly')
    for ticker in tickers:
        status = add_monthly_data_to_database(ticker)
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


def add_monthly_data_to_database(ticker):
    raw_data = alpha_vantage.get_monthly_history(ticker)
    try:
        if raw_data is None:
            return Status.Failed
        if 'Error Message' in raw_data and 'Invalid API call' in raw_data['Error Message']:
            return Status.Invalid
        if 'Note' in raw_data and '500 calls per day' in raw_data['Note']:
            print(raw_data)
            return Status.API_Limit
        ticker = raw_data['Meta Data']['2. Symbol']
    except Exception:
        return Status.Invalid
    monthly_data = raw_data['Monthly Adjusted Time Series']
    first_entry = True
    converted_data = []
    for month in monthly_data:
        if first_entry:  # Skip the current month
            first_entry = False
            continue
        month_data = monthly_data[month]
        row = {
            'ticker': ticker,
            'date': month,
            'price': month_data['5. adjusted close'],
            'dividend': month_data['7. dividend amount']
        }
        converted_data.append(row)
        print(row)
    db.monthly_history_table.add_monthly_data(converted_data)
    return Status.Success


if __name__ == "__main__":
    update_all()
