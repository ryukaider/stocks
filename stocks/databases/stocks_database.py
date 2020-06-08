from databases.database import Database
from databases import tables


class StocksDatabase(Database):
    def __init__(self, name):
        Database.__init__(self, name)

        self.name = name

        self.tickers_table = tables.tickers_table.TickersTable(self.cursor())
        self.api_progress_table = tables.api_progress_table.ApiProgressTable(self.cursor())
        self.company_profile_table = tables.company_profile_table.CompanyProfileTable(self.cursor())
        self.daily_history_table = tables.daily_history_table.DailyHistoryTable(self.cursor())
        self.yearly_history_table = tables.yearly_history_table.YearlyHistoryTable(self.cursor())
        self.dividends_table = tables.dividends_table.DividendsTable(self.cursor())
