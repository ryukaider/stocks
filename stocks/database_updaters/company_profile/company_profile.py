class CompanyProfile():
    def __init__(self,
                 ticker=None,
                 name=None,
                 exchange=None,
                 sector=None,
                 industry=None,
                 description=None,
                 ceo=None,
                 employees=None,
                 website=None,
                 country=None):

        self.ticker = ticker
        self.name = name
        self.exchange = exchange
        self.sector = sector
        self.industry = industry
        self.description = description
        self.ceo = ceo
        self.employees = employees
        self.website = website
        self.country = country
