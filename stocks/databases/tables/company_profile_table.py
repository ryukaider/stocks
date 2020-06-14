from databases import postgres
from .table import Table


class CompanyProfileTable(Table):
    columns = {
        'ticker': 'text PRIMARY KEY NOT NULL',
        'name': 'text',
        'exchange': 'text',
        'sector': 'text',
        'industry': 'text',
        'description': 'text',
        'ceo': 'text',
        'employees': 'numeric',
        'website': 'text',
        'country': 'text',
    }

    def __init__(self, cursor, name='company_profile'):
        Table.__init__(self, cursor, name, self.columns)

    def add_stock(self, ticker):
        row = {'ticker': ticker}
        return postgres.insert_row_as_dict(self.cursor, self.name, row)

    def update_name(self, ticker, name):
        return self.update_value('ticker', ticker, 'name', name)

    def update_exchange(self, ticker, exchange):
        exchange = self._normalize_exchange(exchange)
        return self.update_value('ticker', ticker, 'exchange', exchange)

    @staticmethod
    def _normalize_exchange(exchange):
        try:
            exchange = exchange.upper()
        except Exception:
            pass
        try:
            return {
                None: None,
                'NYSE': 'NYSE',
                'NEW YORK STOCK EXCHANGE': 'NYSE',
                'NASDAQ': 'NASDAQ'
            }[exchange]
        except Exception:
            return exchange

    def update_description(self, ticker, description):
        return self.update_value('ticker', ticker, 'description', description)

    def update_sector(self, ticker, sector):
        sector = self._normalize_sector(sector)
        return self.update_value('ticker', ticker, 'sector', sector)

    @staticmethod
    def _normalize_sector(sector):
        #industry broadcasting = Communication Services
        try:
            return {
                'Communications': 'Communication Services',
                'Consumer Services': 'Consumer Discretionary',
                'Retail Trade': 'Consumer Discretionary',
                'Consumer Durables': 'Consumer Discretionary',
                'Consumer Non-Durables': 'Consumer Staples',
                'Energy Minerals': 'Energy',
                'Health Technology': 'Health Care',
                'Health Services': 'Health Care',
                'Transportation': 'Industrials',
                'Producer Manufacturing': 'Industrials',
                'Industrial Services': 'Industrials',
                #'Commercial Services': 'Industrials', or health care
                'Non-Energy Minerals': 'Materials',
                #'Process Industries': 'Materials', or Consumer Staples
                'Finance': 'Financial Services',
                'Electronic Technology': 'Technology',
                'Technology Services': 'Technology',
                #'Distribution Services': 'Technology' or health care
            }[sector]
        except Exception:
            return sector

    def update_industry(self, ticker, industry):
        return self.update_value('ticker', ticker, 'industry', industry)

    def update_ceo(self, ticker, ceo):
        return self.update_value('ticker', ticker, 'ceo', ceo)

    def update_employees(self, ticker, employees):
        return self.update_value('ticker', ticker, 'employees', employees)

    def update_website(self, ticker, website):
        return self.update_value('ticker', ticker, 'website', website)

    def update_country(self, ticker, country):
        return self.update_value('ticker', ticker, 'country', country)

    def get_name(self, ticker):
        return self.get_value('ticker', ticker, 'name')

    def get_exchange(self, ticker):
        return self.get_value('ticker', ticker, 'exchange')

    def get_sector(self, ticker):
        return self.get_value('ticker', ticker, 'sector')

    def get_industry(self, ticker):
        return self.get_value('ticker', ticker, 'industry')

    def get_description(self, ticker):
        return self.get_value('ticker', ticker, 'description')

    def get_ceo(self, ticker):
        return self.get_value('ticker', ticker, 'ceo')

    def get_employees(self, ticker):
        return self.get_value('ticker', ticker, 'employees')

    def get_website(self, ticker):
        return self.get_value('ticker', ticker, 'website')

    def get_country(self, ticker):
        return self.get_value('ticker', ticker, 'country')
