from ftplib import FTP


def get_all_tickers():
    tickers = []
    tickers.extend(get_nasdaq_tickers())
    tickers.extend(get_nyse_tickers())
    return tickers


def get_nasdaq_tickers():
    nasdaqlisted = _get_nasdaqlisted()
    tickers = _extract_tickers_from_text(nasdaqlisted)
    return tickers


def get_nyse_tickers():
    otherlisted = _get_otherlisted()
    tickers = _extract_tickers_from_text(otherlisted)
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


def _extract_tickers_from_text(text):
    splitdata = text.splitlines()
    splitdata.pop(0)  # Remove header row
    tickers = []
    for line in splitdata:
        ticker = line.split('|')[0]
        tickers.append(ticker)
    return tickers
