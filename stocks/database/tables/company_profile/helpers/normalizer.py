def normalize_rows(rows):
    normalized_rows = []
    for row in rows:
        row['exchange'] = normalize_exchange(row.get('exchange'))
        row['sector'] = normalize_sector(row.get('sector'))
        normalized_rows.append(row)
    return normalized_rows


def normalize_exchange(exchange):
    if exchange is None:
        return exchange

    try:
        exchange = exchange.upper()
    except Exception:
        pass

    try:
        return {
            None: None,
            'NYSE': 'NYSE',
            'NYQ': 'NYSE',
            'NYS': 'NYSE',
            #'ASE': 'NYSE', #  Amman Stock Exchange?
            'NEW YORK STOCK EXCHANGE': 'NYSE',
            'NASDAQ': 'NASDAQ',
            'NMS': 'NASDAQ',
            'NCM': 'NASDAQ',
            'NGM': 'NASDAQ'
        }[exchange]
    except Exception:
        return exchange


def normalize_sector(sector):
    if sector is None:
        return sector

    try:
        return {
            'Communications': 'Communication Services',
            'Consumer Services': 'Consumer Discretionary',
            'Retail Trade': 'Consumer Discretionary',
            'Consumer Durables': 'Consumer Discretionary',
            'Consumer Cyclical': 'Consumer Discretionary',
            'Consumer Non-Durables': 'Consumer Staples',
            'Consumer Defensive': 'Consumer Staples',
            'Energy Minerals': 'Energy',
            'Finance': 'Financial Services',
            'Financial': 'Financial Services',
            'Health Technology': 'Health Care',
            'Health Services': 'Health Care',
            'Healthcare': 'Health Care',
            'Transportation': 'Industrials',
            'Producer Manufacturing': 'Industrials',
            'Industrial Services': 'Industrials',
            'Non-Energy Minerals': 'Materials',
            'Basic Materials': 'Materials',
            'Electronic Technology': 'Technology',
            'Technology Services': 'Technology',
        }[sector]
    except Exception:
        return sector
