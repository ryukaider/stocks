from ftplib import FTP


def get_tickers():
    nasdaqlisted = _get_nasdaqlisted()
    tickers = _extract_tickers_from_nasdaqlisted(nasdaqlisted)
    return tickers


def _get_nasdaqlisted():
    ftp = FTP('ftp.nasdaqtrader.com')
    ftp.login()
    binarydata = []
    ftp.retrbinary("RETR /symboldirectory/nasdaqlisted.txt", callback=binarydata.append)
    stringdata = ''
    for row in binarydata:
        stringdata += row.decode("utf-8")
    return stringdata


def _extract_tickers_from_nasdaqlisted(nasdaqlisted):
    splitdata = nasdaqlisted.splitlines()
    splitdata.pop(0)  # Remove header row
    tickers = []
    for line in splitdata:
        ticker = line.split('|')[0]
        tickers.append(ticker)
    return tickers


if __name__ == '__main__':
    get_tickers()
