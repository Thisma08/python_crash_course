cities = {
    'Bruxelles': {'country': 'Belgium', 'population': '1,209 million'},
    'Paris': {'country': 'France', 'population': '2,161 millions'},
    'Rome': {'country': 'Italy', 'population': '2,873 million'}
}

for city, city_info in cities.items():
    print(f"\n{city}:")
    print(f"\tCountry: {city_info['country']}")
    print(f"\tPopulation: {city_info['population']}")
        