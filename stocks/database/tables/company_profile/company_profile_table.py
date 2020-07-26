from .helpers import normalizer
from ..table.table import Table


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

    def upsert(self, rows):
        primary_keys = ['ticker']
        noramlized_rows = normalizer.normalize_rows(rows)
        return self._upsert_rows(noramlized_rows, primary_keys)

    def update_name(self, ticker, name):
        return self.update_value('ticker', ticker, 'name', name)

    def update_exchange(self, ticker, exchange):
        exchange = normalizer.normalize_exchange(exchange)
        return self.update_value('ticker', ticker, 'exchange', exchange)

    def update_description(self, ticker, description):
        return self.update_value('ticker', ticker, 'description', description)

    def update_sector(self, ticker, sector):
        sector = normalizer.normalize_sector(sector)
        return self.update_value('ticker', ticker, 'sector', sector)

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
