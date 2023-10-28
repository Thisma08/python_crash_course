favorite_places = {
    'Alice': ['Japan'],
    'Mathis': ['Italy', 'Japan', 'France'],
    'Marc': ['France', 'Italy']
}

for name, places in favorite_places.items():
    print(f"{name}'s favorite place(s):")
    for place in places:
        print(f"  {place}")
    print("\n")