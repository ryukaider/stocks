from .database import Database
from .tables.api_progress_table import ApiProgressTable
from database.tables.company_profile.company_profile_table import CompanyProfileTable
from .tables.daily_history_table import DailyHistoryTable
from .tables.dividends_table import DividendsTable
from .tables.table_progress_table import TableProgressTable
from .tables.tickers_table import TickersTable
from .tables.yearly_history_table import YearlyHistoryTable


class StocksDatabase(Database):
    def __init__(self, name=None):
        if name is not None:
            Database.__init__(self, name)
        else:
            Database.__init__(self)

        self.tickers_table = TickersTable(self.cursor())
        self.table_progress_table = TableProgressTable(self.cursor())
        self.api_progress_table = ApiProgressTable(self.cursor())
        self.company_profile_table = CompanyProfileTable(self.cursor())
        self.daily_history_table = DailyHistoryTable(self.cursor())
        self.yearly_history_table = YearlyHistoryTable(self.cursor())
        self.dividends_table = DividendsTable(self.cursor())
