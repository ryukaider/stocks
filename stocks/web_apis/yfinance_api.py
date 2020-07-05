# https://github.com/ranaroussi/yfinance
import yfinance as yf

ko = yf.Ticker('KO')

#info = ko.get_info()

dividends = ko.dividends.to_dict()

for (key, value) in dividends.items():
    print(key, value)
