favorite_numbers = {
    'Mathis': [8],
    'Alice': [42, 87],
    'Marc': [23, 78, 4],
    'Claire': [67]
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite number(s):")
    for number in numbers:
        print(f"  {number}")
    print("\n")