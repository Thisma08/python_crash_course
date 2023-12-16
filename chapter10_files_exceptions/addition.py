try:
    x = input("Entrez un nombre: ")
    x = int(x)

    y = input("Entrez un second nombre: ")
    y = int(y)
except ValueError:
    print("Vous devez entrer un nombre.")
else:
    sum = x + y
    print(f"La somme de {x} et de {y} est {sum}.")