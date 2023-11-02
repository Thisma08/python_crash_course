def make_sandwich(*items):
    for item in items:
        print(f"Ajout de {item}.")
    print("Prêt")

make_sandwich('jambon', 'fromage')
make_sandwich('dinde', 'mayonnaise')
make_sandwich('oeuf', 'salade', 'jambon', 'ketchup')