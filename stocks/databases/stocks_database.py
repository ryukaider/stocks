from databases.database import Database
from databases.tables.api_progress_table import ApiProgressTable
from databases.tables.company_profile_table import CompanyProfileTable
from databases.tables.daily_history_table import DailyHistoryTable
from databases.tables.dividends_table import DividendsTable
from databases.tables.tickers_table import TickersTable
from databases.tables.yearly_history_table import YearlyHistoryTable


class StocksDatabase(Database):
    def __init__(self, name):
        Database.__init__(self, name)

        self.name = name

        self.tickers_table = TickersTable(self.cursor())
        self.api_progress_table = ApiProgressTable(self.cursor())
        self.company_profile_table = CompanyProfileTable(self.cursor())
        self.daily_history_table = DailyHistoryTable(self.cursor())
        self.yearly_history_table = YearlyHistoryTable(self.cursor())
        self.dividends_table = DividendsTable(self.cursor())
