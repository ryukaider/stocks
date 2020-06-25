select * from tickers
where ticker = 'ZYME'

select * from api_progress
--where company_profile is NULL
order by company_profile asc

select distinct exchange from company_profile
JOIN tickers ON company_profile.ticker=tickers.ticker

select * from company_profile
JOIN tickers ON company_profile.ticker=tickers.ticker
where exchange IS NULL
and employees is not NULL
order by employees desc

select * from company_profile
where exchange = 'NYSE AMERICAN'
and employees is not NULL
order by employees desc
where exchange = 'NYSE ARCA'
where exchange IS NULL
