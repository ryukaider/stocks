from web_apis import financial_modeling_prep


def test_get_company_profile():
    response = financial_modeling_prep.get_company_profile('MSFT')
    assert response is not None
    assert response['price'] is not None
    assert response['beta'] is not None
    assert response['volAvg'] is not None
    assert response['mktCap'] is not None
    assert response['lastDiv'] is not None
    assert response['range'] is not None
    assert response['changes'] is not None
    assert response['changesPercentage'] is not None
    assert response['companyName'] == 'Microsoft Corporation'
    assert response['exchange'] is not None
    assert response['industry'] == 'Application Software'
    assert response['website'] == 'http://www.microsoft.com'
    assert response['description'] is not None
    assert response['ceo'] is not None
    assert response['sector'] == 'Technology'
    assert response['image'] is not None


def test_get_company_profile_invalid():
    response = financial_modeling_prep.get_company_profile('invalid')
    assert response is None