from ..model.company_profile import CompanyProfile
from web_apis import iex


class IexCompanyProfileConverter:

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
