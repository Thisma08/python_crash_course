party_size = input("Taille du groupe? ")
party_size = int(party_size)

if party_size > 8:
    print("Desolé, vous devez attendre pour une table.")
else:
    print("Votre table est prete.")