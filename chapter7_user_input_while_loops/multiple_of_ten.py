number = input("Entrez un nombre: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} est un multiple de 10.")
else:
    print(f"{number} n'est pas un multiple de 10.")