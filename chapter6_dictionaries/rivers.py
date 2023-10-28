rivers = {
    'meuse': 'belgium',
    'nile': 'egypt',
    'hudson': 'united states'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\n")
for river in rivers.keys():
    print(river)

print("\n")
for country in rivers.values():
    print(country)