from ..model.company_profile import CompanyProfile
import yfinance as yf


class YahooCompanyProfileConverter:

    def get_company_profile(self, ticker) -> CompanyProfile:
        try:
            info = yf.Ticker(ticker).info
        except:
            return None

        if info is None:
            return None

        return CompanyProfile(
            ticker=ticker,
            name=info.get('longName', None),
            exchange=info.get('exchange', None),
            sector=info.get('sector', None),
            industry=info.get('industry', None),
            description=info.get('longBusinessSummary', None),
            employees=info.get('fullTimeEmployees', None),
            website=info.get('website', None),
            country=info.get('country', None)
        )
