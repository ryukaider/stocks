from web_apis import iex


def test_get_company_profile():
    profile = iex.get_company_profile('AAPL')
    assert profile is not None
    assert profile['symbol'] == 'AAPL'
    assert profile['companyName'] == 'Apple, Inc.'
    assert profile['exchange'] == 'NASDAQ'
    assert profile['industry'] == 'Telecommunications Equipment'
    assert profile['website'] == 'http://www.apple.com'
    assert profile['description'] is not None
    assert profile['CEO'] == 'Timothy Donald Cook'
    assert profile['securityName'] == 'Apple Inc.'
    assert profile['issueType'] == 'cs'
    assert profile['sector'] == 'Electronic Technology'
    assert profile['primarySicCode'] == 3663
    assert profile['employees'] > 100000
    assert profile['tags'] == ['Electronic Technology', 'Telecommunications Equipment']
    assert profile['address'] == 'One Apple Park Way'
    assert profile['address2'] is None
    assert profile['state'] == 'CA'
    assert profile['city'] == 'Cupertino'
    assert profile['zip'] == '95014-2083'
    assert profile['country'] == 'US'
    assert profile['phone'] is not None
