from .company_profile import CompanyProfile
from web_apis import iex


class IexCompanyProfileConverter:

    def get_company_profiles(self, tickers) -> list:
        company_profiles = []
        for ticker in tickers:
            company_profile = self.get_company_profile(ticker)
            if company_profile is not None:
                company_profiles.append(company_profile)
        return company_profiles

    def get_company_profile(self, ticker) -> CompanyProfile:
        profile = iex.get_company_profile(ticker)

        if profile is None:
            return None

        return CompanyProfile(
            ticker=ticker,
            name=profile['companyName'],
            exchange=profile['exchange'],
            sector=profile['sector'],
            industry=profile['industry'],
            description=profile['description'],
            ceo=profile['CEO'],
            employees=profile['employees'],
            website=profile['website'],
            country=profile['country']
        )
