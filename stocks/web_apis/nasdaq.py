from ftplib import FTP


def get_all_tickers():
    tickers = []
    tickers.extend(get_nasdaq_tickers())
    tickers.extend(get_nyse_tickers())
    if tickers is None or len(tickers) == 0:
        raise Exception('Failed to retrieve tickers from Nasdaq FTP site')
    return tickers


def get_nasdaq_tickers():
    nasdaqlisted = _get_nasdaqlisted()
    nasdaq_stocks = _deserialize_nasdaqlisted(nasdaqlisted)
    filtered_stocks = _filter_stocks(nasdaq_stocks)
    tickers = _extract_tickers_from_stocks(filtered_stocks, 'symbol')
    return tickers


def get_nyse_tickers():
    otherlisted = _get_otherlisted()
    otherlisted_stocks = _deserialize_otherlisted(otherlisted)
    filtered_stocks = _filter_stocks(otherlisted_stocks)
    tickers = _extract_tickers_from_stocks(filtered_stocks, 'nasdaq symbol')
    return tickers


def _get_nasdaqlisted():
    return _get_text_from_ftp('nasdaqlisted.txt')


def _get_otherlisted():
    return _get_text_from_ftp('otherlisted.txt')


def _get_text_from_ftp(filename):
    ftp = FTP('ftp.nasdaqtrader.com')
    ftp.login()
    binarydata = []
    ftp.retrbinary(f'RETR /symboldirectory/{filename}', callback=binarydata.append)
    text = ''
    for row in binarydata:
        text += row.decode("utf-8")
    return text


def _deserialize_nasdaqlisted(text):
    splitdata = text.splitlines()
    splitdata.pop(0)  # Remove header row
    splitdata.pop(-1)  # Remove file creation row
    stocks = []
    for line in splitdata:
        splitline = line.split('|')
        stock = {
            'symbol': splitline[0],
            'name': splitline[1],
            'market category': splitline[2],
            'test issue': splitline[3],
            'financial status': splitline[4],
            'round lot size': splitline[5],
            'etf': splitline[6],
            'nextshares': splitline[7]
        }
        stocks.append(stock)
    return stocks


def _deserialize_otherlisted(text):
    splitdata = text.splitlines()
    splitdata.pop(0)  # Remove header row
    splitdata.pop(-1)  # Remove file creation row
    stocks = []
    for line in splitdata:
        try:
            splitline = line.split('|')
            stock = {
                'act symbol': splitline[0],
                'name': splitline[1],
                'exchange': splitline[2],
                'cqs symbol': splitline[3],
                'etf': splitline[4],
                'round lot size': splitline[5],
                'test issue': splitline[6],
                'nasdaq symbol': splitline[7]
            }
            stocks.append(stock)
        except IndexError:
            continue
    return stocks


def _filter_stocks(stocks):
    filter_stocks = []
    for stock in stocks:
        if stock['test issue'] == 'Y' or stock['etf'] == 'Y':
            continue
        try:
            if stock['exchange'] == 'Z' or stock['exchange'] == 'V' or stock['exchange'] == 'P':
                continue
        except KeyError:
            pass
        filter_stocks.append(stock)
    return filter_stocks


def _extract_tickers_from_stocks(stocks, ticker_key):
    tickers = []
    for stock in stocks:
        tickers.append(stock[ticker_key])
    return tickers
