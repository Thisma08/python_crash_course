brands = ["Opel", "Nissan", "Renault"]
for brand in brands:
    if brand[0].upper() in ["A", "E", "I", "O", "U", "Y"]:
        print(f"I ride in an {brand}")
    else:
        print(f"I ride in a {brand}")