print("Entrez 'q' pour quitter.\n")

while True:
    try:
        x = input("\nEntrez un nombre: ")
        if x == 'q':
            break
        x = int(x)

        y = input("Entrez un second nombre: ")
        if y == 'q':
            break
        y = int(y)

    except ValueError:
        print("Vous devez entrer un nombre.")

    else:
        sum = x + y
        print(f"La somme de {x} et de {y} est {sum}.")