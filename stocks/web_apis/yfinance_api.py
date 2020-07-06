# https://github.com/ranaroussi/yfinance
import yfinance as yf

ticker = yf.Ticker('MSFT')

info = ticker.get_info()

for (key, value) in info.items():
    print(key, value)
