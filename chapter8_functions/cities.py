def describe_city(city, country='chili'):
    msg = f"{city.title()} est au {country.title()}."
    print(msg)

describe_city('santiago')
describe_city('reykjavik', 'islande')
describe_city('punta arenas')