def city_country(city, country):
    return f"{city.title()}, {country.title()}"

city = city_country('santiago', 'chili')
print(city)

city = city_country('ushuaia', 'argentine')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)