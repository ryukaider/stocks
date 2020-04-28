import os, sys
_root_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(_root_path)

import time
from enum import Enum
from web_apis import alpha_vantage
from database.tables.monthly_history_table import MonthlyHistoryTable
from database.tables.api_progress_table import ApiProgressTable

monthly_history_table = MonthlyHistoryTable()
api_progress_table = ApiProgressTable()


class Status(Enum):
    Success = 0
    Failed = 1
    Invalid = 2
    API_Limit = 3


def update():
    tickers = api_progress_table.get_incomplete_stocks('monthly')
    for ticker in tickers:
        status = add_monthly_data_to_database(ticker)
        print(status)
        if status == Status.Success or status == Status.Invalid:
            api_progress_table.set_monthly_done(ticker)
            time.sleep(15) # API limits 5 calls per minute
            continue
        if status == Status.Failed:
            continue
        if status == Status.API_Limit:
            print('Stopping due to reaching APi limit')
            break


def add_monthly_data_to_database(ticker):
    raw_data = alpha_vantage.get_monthly_data(ticker)
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
        if first_entry: # Skip the current month
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
    monthly_history_table.add_monthly_data(converted_data)
    return Status.Success


if __name__ == "__main__":
    update()
