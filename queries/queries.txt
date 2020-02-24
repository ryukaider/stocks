select * from current_data
where dividend_yield is not null
and dividend_years_increasing >= 5
and payout_ratio_ttm < 90
and payout_ratio_ttm > 0
order by dividend_yield desc
